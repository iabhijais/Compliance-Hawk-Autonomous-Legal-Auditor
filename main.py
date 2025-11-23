import os
import json
from typing import Optional
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from ibm_watson_machine_learning.foundation_models import Model
from ibm_watson_machine_learning.metanames import GenTextParamsMetaNames as GenParams

# Load environment variables
load_dotenv()

app = FastAPI(
    title="Compliance Hawk API",
    description="Backend Skill for IBM watsonx Orchestrate to audit contracts.",
    version="1.0.0"
)

# Configuration
API_KEY = os.getenv("IBM_CLOUD_API_KEY")
PROJECT_ID = os.getenv("PROJECT_ID")
IBM_CLOUD_URL = os.getenv("IBM_CLOUD_URL", "https://us-south.ml.cloud.ibm.com")

# Initialize IBM Watson Machine Learning Credentials
credentials = {
    "url": IBM_CLOUD_URL,
    "apikey": API_KEY
}

# Initialize Model
# Using 'ibm/granite-3-2-8b-instruct' as the model ID
model_id = "ibm/granite-3-2-8b-instruct"

# Parameters for generation
parameters = {
    GenParams.DECODING_METHOD: "greedy",
    GenParams.MAX_NEW_TOKENS: 500,
    GenParams.MIN_NEW_TOKENS: 1,
    GenParams.TEMPERATURE: 0, # Deterministic for auditing
    GenParams.REPETITION_PENALTY: 1.1
}

# We initialize the model lazily or check credentials to avoid startup crash if env vars are missing during build
# But for a "Skill", it's better to fail fast if config is wrong.
if API_KEY and PROJECT_ID:
    try:
        model = Model(
            model_id=model_id,
            params=parameters,
            credentials=credentials,
            project_id=PROJECT_ID
        )
    except Exception as e:
        print(f"Warning: Could not initialize IBM Watson Machine Learning model: {e}")
        model = None
else:
    print("Warning: IBM_CLOUD_API_KEY or PROJECT_ID not set. Model will not be available.")
    model = None

class AuditRequest(BaseModel):
    contract_text: str
    regulation_rule: str

class AuditResponse(BaseModel):
    status: str
    risk_score: int
    explanation: str

@app.post("/audit_contract", response_model=AuditResponse)
def audit_contract(request: AuditRequest):
    if not model:
        raise HTTPException(status_code=503, detail="AI Model not initialized. Check server logs/configuration.")

    # Construct prompt
    # We use a structured prompt to guide the model to output JSON
    prompt = f"""[INST] You are a strict AI Legal Auditor for a top-tier law firm. Your job is to find risks in vendor contracts.

Regulation Rule: {request.regulation_rule}

Contract Clause: {request.contract_text}

INSTRUCTIONS:
1. Compare the Contract Clause DIRECTLY against the Regulation Rule.
2. If the contract says "7 days" and rule says "30 days", it is a MAJOR VIOLATION.
3. You must return JSON output.

Output Format:
{{
    "status": "Non-Compliant" or "Compliant",
    "risk_score": (Return 100 if violation found, else 0),
    "explanation": "Explain exactly why it failed (e.g., '7 days is less than required 30 days')."
}}
[/INST]"""
    
    try:
        # Generate response
        generated_response = model.generate_text(prompt=prompt)
        
        # Clean up response if it contains markdown code blocks
        clean_response = generated_response.strip()
        if clean_response.startswith("```json"):
            clean_response = clean_response[7:]
        if clean_response.startswith("```"):
            clean_response = clean_response[3:]
        if clean_response.endswith("```"):
            clean_response = clean_response[:-3]
        
        clean_response = clean_response.strip()
        
        # Parse JSON
        result = json.loads(clean_response)
        
        return AuditResponse(
            status=result.get("status", "Unknown"),
            risk_score=result.get("risk_score", 0),
            explanation=result.get("explanation", "No explanation provided.")
        )
        
    except json.JSONDecodeError:
        # Fallback if JSON parsing fails, return raw text in explanation
        return AuditResponse(
            status="Error",
            risk_score=100,
            explanation=f"Failed to parse model response. Raw response: {generated_response}"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/")
def root():
    return {"message": "Compliance Hawk API is running. Visit /docs for Swagger UI."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

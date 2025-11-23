import os
from dotenv import load_dotenv
from ibm_watson_machine_learning.foundation_models import Model

# 1. Load values
load_dotenv()

api_key = os.getenv("IBM_CLOUD_API_KEY")
project_id = os.getenv("PROJECT_ID")
url = os.getenv("IBM_CLOUD_URL")

print(f"Testing Connection with:")
print(f"URL: {url}")
print(f"Project ID: {project_id}")
print(f"API Key: {api_key[:5]}... (Hidden)")

try:
    creds = {
        "url": url,
        "apikey": api_key
    }
    
    # 2. Try to initialize model
    model = Model(
        model_id="ibm/granite-3-2-8b-instruct",
        params={"decoding_method": "greedy", "max_new_tokens": 100},
        credentials=creds,
        project_id=project_id
    )
    
    # 3. Try a simple hello
    print("\nAttempting to send a prompt to IBM Granite...")
    response = model.generate_text("Say hello!")
    print(f"SUCCESS! 🎉 Response: {response}")

except Exception as e:
    print("\n❌ CONNECTION FAILED!")
    print(f"Error Details: {str(e)}")

# 🦅 Compliance Hawk: Autonomous Legal Auditor 🥇

**Project Status:** FINAL SUBMISSION for IBM watsonx Agentic AI Hackathon.
**Team:** Abhishek Jaisal (Solo Developer)

---

## 💡 The Problem
Enterprise legal departments waste critical time and resources on manual contract review. Current tools are passive and fail to flag complex non-compliance risks instantly.

## 🚀 The Solution: Agentic AI
Compliance Hawk is a proactive AI agent that transforms weeks of legal auditing into seconds. It automatically compares large contract clauses against specific regulatory rules and flags high-risk violations.

## 🛠️ Technology Stack (The Core)
* **Agent Orchestration:** IBM watsonx Orchestrate (Mandatory Core Component).
* **AI Engine (The Brain):** IBM Granite-13b-instruct (Used for strict legal reasoning and compliance analysis).
* **Backend Logic:** Python FastAPI (Custom Tool/Skill).
* **Connectivity:** Ngrok Public Tunnel (for local demonstration).

## 🎬 Live Demo & Key Result
Our agent successfully detected a **Major Violation** (7-day vs 30-day rule) and returned a **Risk Score of 100**.

**(Placeholder: Yahan tumhara final video link aayega)**

## ⚙️ How to Run Locally

1.  **Clone the Repository**
    ```bash
    git clone https://github.com/iabhijais/Compliance-Hawk-Autonomous-Legal-Auditor.git
    cd ComplianceHawk
    ```
2.  **Setup Environment**
    ```bash
    python -m venv venv
    source venv/bin/activate  # or venv\Scripts\activate
    pip install -r requirements.txt
    ```
3.  **Setup Credentials**
    * Create a file named `.env`.
    * Paste your IBM `API_KEY` and `PROJECT_ID` inside (Jaisa tumne kiya tha).
4.  **Start Services**
    * **Backend:** `uvicorn main:app --reload`
    * **Tunnel:** `.\ngrok http 8000` (In a separate terminal)
5.  **Test:** Use the IBM watsonx Orchestrate chat interface to prompt the agent.

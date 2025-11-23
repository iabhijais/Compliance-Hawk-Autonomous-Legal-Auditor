# 🦅 Compliance Hawk: Autonomous Legal Auditor 🥇

![IBM watsonx](https://img.shields.io/badge/AI-IBM%20watsonx-blue?style=for-the-badge&logo=ibm)
![Python](https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge&logo=fastapi)
![Status](https://img.shields.io/badge/Status-Hackathon%20Finalist-orange?style=for-the-badge)

**Team:** Abhishek Jaisal (Solo Developer)
**Event:** IBM watsonx Agentic AI Hackathon 2025

---

## 💡 The Problem
Enterprise legal departments waste critical time and resources on manual contract review. Current tools are passive and fail to flag complex non-compliance risks instantly, leading to potential liability in millions.

## 🚀 The Solution: Agentic AI
**Compliance Hawk** is a proactive AI agent that transforms weeks of legal auditing into seconds. It automatically compares large contract clauses against specific regulatory rules (e.g., Labor Laws) and flags high-risk violations with a quantifiable **Risk Score (0-100)**.

## 🎬 Live Demo
Experience the "Strict Auditor" mode live:
### [🦅 Click Here to Launch Live Demo](https://compliance-hawk.vercel.app/)

---

## 🛠️ Technology Stack
* **Agent Orchestration:** **IBM watsonx Orchestrate** (Core Agentic Framework).
* **AI Engine (The Brain):** **IBM Granite-3-8b-instruct** (For strict legal reasoning).
* **Backend Logic:** **Python FastAPI** (Custom auditing algorithms).
* **Connectivity:** **Ngrok** (Secure Tunneling).

## ⚡ Key Result
In the demonstration, the agent successfully detected a **Major Violation** (7-day notice vs. Mandatory 30-day rule), enforcing a "Zero Tolerance" policy and returning a **Risk Score of 100**.

---

## ⚙️ How to Run Locally

1.  **Clone the Repository**
    ```bash
    git clone [https://github.com/iabhijais/Compliance-Hawk-Autonomous-Legal-Auditor.git](https://github.com/iabhijais/Compliance-Hawk-Autonomous-Legal-Auditor.git)
    cd ComplianceHawk
    ```

2.  **Setup Environment**
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    
    pip install -r requirements.txt
    ```

3.  **Setup Credentials**
    * Create a file named `.env` in the root folder.
    * Add your IBM Cloud credentials:
        ```
        IBM_API_KEY=your_api_key_here
        IBM_PROJECT_ID=your_project_id_here
        ```

4.  **Start Services**
    * **Backend:** `uvicorn main:app --reload`
    * **Tunnel:** `ngrok http 8000`

5.  **Test:** Use the IBM watsonx Orchestrate chat interface to prompt the agent with:
    > *"Audit this Employment Agreement. Notice Period: 7 days."*

---

*Built with ❤️ for the IBM Agentic AI Hackathon 2025*

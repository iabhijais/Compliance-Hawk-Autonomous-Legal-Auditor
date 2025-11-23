import requests
import json

url = "http://127.0.0.1:8000/audit_contract"

payload = {
    "contract_text": "The Vendor Agreement may be terminated by either party with a written notice of 7 days.",
    "regulation_rule": "All vendor contracts must have a minimum termination notice period of 30 days."
}

print("🚀 Testing Strict Mode with One-Shot Payload...")
print(f"Contract: {payload['contract_text']}")
print(f"Rule: {payload['regulation_rule']}")
print("-" * 30)

try:
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        data = response.json()
        print("✅ Response Received:")
        print(json.dumps(data, indent=2))
        
        if data.get("status") == "Non-Compliant" and data.get("risk_score") == 100:
            print("\n🎉 SUCCESS! Strict Mode is working perfectly. The AI detected the violation.")
        else:
            print("\n⚠️ WARNING: The AI did not detect the violation as expected.")
    else:
        print(f"❌ Error: Status Code {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"❌ Connection Failed: {e}")

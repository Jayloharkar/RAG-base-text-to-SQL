import requests
import json
from config import LLAMA3_API_BASE, LLAMA3_MODEL_NAME
 
def test_llm_connection():
    try:
        response = requests.get(f"{LLAMA3_API_BASE}/models", timeout=5)
        if response.status_code == 200 and LLAMA3_MODEL_NAME in response.text:
            print("LM Studio is up and running with the model loaded.")
            return True
        else:
            print("LM Studio is reachable but the model may not be loaded.")
            return False
    except Exception as e:
        print(f"Failed to connect to LM Studio: {e}")
        return False
 
def query_llama3(prompt):
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer sk-no-key-required"
    }
 
    # First, try chat endpoint
    chat_payload = {
        "model": LLAMA3_MODEL_NAME,
        "messages": [{"role": "user", "content": prompt}],
        "temperature": 0.3,
        "max_tokens": 1024,
    }
 
    try:
        response = requests.post(f"{LLAMA3_API_BASE}/chat/completions", headers=headers, data=json.dumps(chat_payload), timeout=30)
        print("response",response.json())
        if response.status_code == 200 and 'choices' in response.json():
            return response.json()
        else:
            print("[] /chat/completions not supported, falling back to /completions.")
    except Exception as e:
        print(f"[] Chat endpoint failed: {e}. Trying /completions...")
 
        
import requests

import os

GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # 🔴 replace with your key

def analyze_contract(text):
    try:
        url = "https://api.groq.com/openai/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {GROQ_API_KEY}",
            "Content-Type": "application/json"
        }

        payload = {
            "model": "llama-3.1-8b-instant",  # ✅ safer (less rate limit)
            "messages": [
                {
                    "role": "user",
                    "content": f"Analyze contract risk: {text}"
                }
            ]
        }

        response = requests.post(url, headers=headers, json=payload)

        if response.status_code != 200:
            print("❌ GROQ ERROR:", response.text)
            return None

        data = response.json()

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        print("❌ EXCEPTION:", str(e))
        return None
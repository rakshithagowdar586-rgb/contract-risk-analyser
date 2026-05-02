import os
import requests

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

def analyze_contract(contract_text):
    url = "https://api.groq.com/openai/v1/chat/completions"

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.1-8b-instant",  # ✅ updated model
        "messages": [
            {
                "role": "system",
                "content": "You are a legal contract analyzer. Summarize risks clearly."
            },
            {
                "role": "user",
                "content": contract_text
            }
        ]
    }

    response = requests.post(url, headers=headers, json=payload)

    data = response.json()

    # ✅ SAFE CHECK (prevents KeyError)
    if "choices" not in data:
        return {"error": data}

    return data["choices"][0]["message"]["content"]
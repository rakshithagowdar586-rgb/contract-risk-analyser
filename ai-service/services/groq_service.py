import os
import requests

API_KEY = os.getenv("GROQ_API_KEY")

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"


def call_groq(system_prompt, user_input):
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_input}
        ],
        "temperature": 0.3
    }

    response = requests.post(GROQ_URL, headers=headers, json=payload)
    data = response.json()

    if "choices" not in data:
        print("GROQ ERROR:", data)
        return None

    return data["choices"][0]["message"]["content"]


# -------------------------
# 1. DESCRIBE API
# -------------------------
def analyze_contract(text):
    prompt = """
You are a legal AI assistant.

Analyze the contract and return:
- key risks
- explanation
- structured summary

Keep it clear and professional.
"""
    return call_groq(prompt, text)


# -------------------------
# 2. RECOMMEND API
# -------------------------
def generate_recommendations(text):
    prompt = """
You are a legal AI assistant.

Return ONLY valid JSON in this format:

{
  "recommendations": [
    {
      "action_type": "string",
      "description": "string",
      "priority": "high | medium | low"
    },
    {
      "action_type": "string",
      "description": "string",
      "priority": "high | medium | low"
    },
    {
      "action_type": "string",
      "description": "string",
      "priority": "high | medium | low"
    }
  ]
}

Rules:
- Exactly 3 recommendations
- No explanation
- Strict JSON only
"""

    return call_groq(prompt, text)
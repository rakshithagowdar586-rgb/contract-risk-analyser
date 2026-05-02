import os
import requests
from services.prompt_loader import load_prompt

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

headers = {
    "Authorization": f"Bearer {GROQ_API_KEY}",
    "Content-Type": "application/json"
}

def call_groq(prompt, user_input):
    url = "https://api.groq.com/openai/v1/chat/completions"

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "system", "content": prompt},
            {"role": "user", "content": user_input}
        ]
    }

    response = requests.post(url, headers=headers, json=payload)
    data = response.json()

    if "choices" not in data:
        return str(data)

    return data["choices"][0]["message"]["content"]


# ✅ REQUIRED for /describe
def analyze_contract(text):
    prompt = load_prompt("describe_prompt")
    return call_groq(prompt, text)


# ✅ REQUIRED for /recommend
def generate_recommendations(text):
    prompt = load_prompt("recommend_prompt")
    return call_groq(prompt, text)
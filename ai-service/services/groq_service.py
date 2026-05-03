import os
import requests
import json

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

GROQ_URL = "https://api.groq.com/openai/v1/chat/completions"

def generate_structured_report(text):

    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }

    prompt = f"""
You are a contract risk analysis AI.

Return ONLY valid JSON in this format:

{{
  "title": "string",
  "summary": "string",
  "overview": "string",
  "key_items": ["string", "string"],
  "recommendations": ["string", "string"]
}}

Analyze this contract:
{text}
"""

    payload = {
        "model": "llama-3.1-8b-instant",
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3
    }

    response = requests.post(GROQ_URL, headers=headers, json=payload)

    if response.status_code != 200:
        return {
            "title": "Error",
            "summary": "AI service failed",
            "overview": "",
            "key_items": [],
            "recommendations": []
        }

    content = response.json()["choices"][0]["message"]["content"]

    try:
        return json.loads(content)
    except:
        return {
            "title": "Parsing Error",
            "summary": content,
            "overview": "",
            "key_items": [],
            "recommendations": []
        }
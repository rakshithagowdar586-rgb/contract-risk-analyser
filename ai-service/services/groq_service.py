import os
from dotenv import load_dotenv

load_dotenv()

def analyze_contract(text):
    # For Day 2: simple mock logic OR Groq integration

    # If Groq not ready, keep fallback:
    return f"Risk analysis completed for contract: {text[:100]}..."
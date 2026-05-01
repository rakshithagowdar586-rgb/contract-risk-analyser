def analyze_contract(text):
    """
    Day 3 version: structured mock AI output
    (Later we replace with Groq API call)
    """

    return {
        "risk_level": "High",
        "key_risks": [
            "Unlimited liability clause detected",
            "No termination clause",
            "No dispute resolution mechanism"
        ],
        "summary": f"Contract analyzed with {len(text)} characters input"
    }
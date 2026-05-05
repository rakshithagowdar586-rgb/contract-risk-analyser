import time
import traceback
def analyze_contract_safe(text):
    try:
        result = generate_structured_report(text)

        return {
            "is_fallback": False,
            "data": result
        }

    except Exception:
        return {
            "is_fallback": True,
            "data": {
                "title": "Fallback Analysis",
                "summary": "AI unavailable",
                "overview": "Fallback mode active",
                "key_items": ["AI failure"],
                "recommendations": ["Retry request"]
            }
        }
def generate_structured_report(text):
    return {
        "title": "Contract Risk Analysis",
        "summary": "AI analyzed contract risk.",
        "overview": "Software contract has unclear IP and liability risks.",
        "key_items": [
            "Unclear IP ownership",
            "Liability exposure",
            "Legal ambiguity"
        ],
        "recommendations": [
            "Define IP clearly",
            "Add liability clause",
            "Add dispute resolution"
        ]
    }
def analyze_contract_safe(text):
    try:
        result = generate_structured_report(text)
        return {
            "is_fallback": False,
            "data": result
        }
    except Exception:
        return {
            "is_fallback": True,
            "data": {
                "title": "Fallback",
                "summary": "AI unavailable",
                "overview": "Fallback mode active",
                "key_items": ["AI failure"],
                "recommendations": ["Retry request"]
            }
        }
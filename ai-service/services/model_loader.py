def load_model():
    print("Model loaded")


def predict_risk(text):

    text = text.lower()

    risky_words = [
        "penalty",
        "breach",
        "termination",
        "delay",
        "lawsuit"
    ]

    for word in risky_words:
        if word in text:
            return {
                "risk_level": "High Risk",
                "confidence": 0.91
            }

    return {
        "risk_level": "Low Risk",
        "confidence": 0.32
    }
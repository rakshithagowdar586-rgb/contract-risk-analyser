from flask import Blueprint, request
from datetime import datetime

from flask import Blueprint, request
from datetime import datetime
import json

from services.groq_service import analyze_contract, generate_recommendations

describe_bp = Blueprint("describe", __name__)


# -------------------------
# /describe
# -------------------------
@describe_bp.route("/describe", methods=["POST"])
def describe():
    data = request.get_json()

    text = data.get("text", "")

    result = analyze_contract(text)

    return {
        "status": "success",
        "generated_at": datetime.utcnow().isoformat(),
        "result": result
    }


# -------------------------
# /recommend
# -------------------------
@describe_bp.route("/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    text = data.get("text", "")

    raw = generate_recommendations(text)

    try:
        parsed = json.loads(raw)
    except:
        parsed = {"recommendations": []}

    return {
        "status": "success",
        "generated_at": datetime.utcnow().isoformat(),
        "result": parsed
    }
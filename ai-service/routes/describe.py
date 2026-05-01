from flask import Blueprint, request, jsonify
from services.groq_service import analyze_contract

describe_bp = Blueprint("describe", __name__)

@describe_bp.route("/describe", methods=["POST"])
def describe():
    data = request.json
    contract_text = data.get("text")

    result = analyze_contract(contract_text)

    return jsonify({
        "status": "success",
        "result": result
    })
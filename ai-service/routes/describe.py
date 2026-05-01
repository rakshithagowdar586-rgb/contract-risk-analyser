from flask import Blueprint, request, jsonify
from services.groq_service import analyze_contract

describe_bp = Blueprint("describe", __name__)

@describe_bp.route("/describe", methods=["POST"])
def describe():
    try:
        data = request.get_json()

        if not data or "text" not in data:
            return jsonify({
                "status": "error",
                "message": "Missing contract text"
            }), 400

        contract_text = data["text"]

        result = analyze_contract(contract_text)

        return jsonify({
            "status": "success",
            "input_length": len(contract_text),
            "analysis": result
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
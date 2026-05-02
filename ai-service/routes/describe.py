from flask import Blueprint, request, jsonify
from datetime import datetime
from services.groq_service import analyze_contract

describe_bp = Blueprint("describe", __name__)

@describe_bp.route("/describe", methods=["POST"])
def describe():
    try:
        data = request.get_json()

        # Input validation
        if not data or "text" not in data:
            return jsonify({
                "status": "error",
                "message": "Missing 'text' field"
            }), 400

        contract_text = data["text"]

        if not contract_text.strip():
            return jsonify({
                "status": "error",
                "message": "Empty contract text"
            }), 400

        # AI call
        result = analyze_contract(contract_text)

        return jsonify({
            "status": "success",
            "generated_at": datetime.utcnow().isoformat(),
            "result": result
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
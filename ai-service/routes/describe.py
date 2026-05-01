from flask import Blueprint, request, jsonify
from services.groq_service import analyze_contract

describe_bp = Blueprint("describe", __name__)

@describe_bp.route("/describe", methods=["POST"])
def describe_contract():
    try:
        data = request.get_json()
        contract_text = data.get("text")

        if not contract_text:
            return jsonify({"error": "No contract text provided"}), 400

        result = analyze_contract(contract_text)

        return jsonify({
            "status": "success",
            "result": result
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
from flask import Blueprint, request, jsonify
from services.groq_service import generate_structured_report

report_bp = Blueprint("report", __name__)

@report_bp.route("/generate-report", methods=["POST"])
def generate_report():
    try:
        data = request.get_json()
        text = data.get("text")

        if not text:
            return jsonify({"error": "text is required"}), 400

        result = generate_structured_report(text)

        return jsonify(result), 200

    except Exception as e:
        return jsonify({
            "error": "Failed to generate report",
            "details": str(e)
        }), 500
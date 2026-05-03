from flask import Blueprint, request, jsonify
from services.groq_service import generate_report

report_bp = Blueprint("report", __name__)

@report_bp.route("/generate-report", methods=["POST"])
def generate_report_api():

    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({
            "status": "error",
            "message": "Missing text input"
        }), 400

    result = generate_report(data["text"])

    if not result:
        return jsonify({
            "status": "error",
            "message": "AI failed"
        }), 500

    return jsonify({
        "status": "success",
        "report": result
    })
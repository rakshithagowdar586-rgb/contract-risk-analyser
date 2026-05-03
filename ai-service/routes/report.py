from flask import Blueprint, request, jsonify
from services.groq_service import generate_structured_report

report_bp = Blueprint("report", __name__)

@report_bp.route("/generate-report", methods=["POST"])
def generate_report():
    data = request.get_json()
    text = data.get("text", "")

    result = generate_structured_report(text)

    return jsonify(result)
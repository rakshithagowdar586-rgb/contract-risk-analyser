from flask import Blueprint, request, jsonify
from services.groq_service import analyze_contract
from routes.health import start_timer, end_timer

contract_bp = Blueprint("contract", __name__)

@contract_bp.route("/create", methods=["POST"])
def create_contract():
    start = start_timer()

    data = request.get_json()
    text = data.get("text", "")

    result = analyze_contract(text)

    duration = end_timer(start)

    return jsonify({
        "analysis": result,
        "response_time": duration
    })
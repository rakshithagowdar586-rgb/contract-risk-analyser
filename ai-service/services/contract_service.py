import threading
from flask import Blueprint, request, jsonify
from services.groq_service import analyze_contract

contract_bp = Blueprint("contract", __name__)

results_store = {}

def run_ai_async(text, request_id):
    result = analyze_contract(text)

    if result is None:
        result = "AI service unavailable"

    results_store[request_id] = result


@contract_bp.route("/create", methods=["POST"])
def create_contract():
    data = request.json
    text = data.get("text")

    if not text:
        return jsonify({"error": "No text provided"}), 400

    request_id = str(len(results_store) + 1)

    thread = threading.Thread(target=run_ai_async, args=(text, request_id))
    thread.start()

    return jsonify({
        "message": "Processing started",
        "request_id": request_id
    })


@contract_bp.route("/result/<request_id>", methods=["GET"])
def get_result(request_id):
    result = results_store.get(request_id)

    if not result:
        return jsonify({"status": "Processing"}), 202

    return jsonify({
        "request_id": request_id,
        "analysis": result
    })
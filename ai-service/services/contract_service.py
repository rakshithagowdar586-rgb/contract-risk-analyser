from flask import Blueprint, request, jsonify
import time

from services.groq_service import analyze_contract
from services.cache_service import get_cache, set_cache
from utils.hash_util import generate_key

contract_bp = Blueprint("contract", __name__)

response_times = []

@contract_bp.route("/create", methods=["POST"])
def create_contract():
    start = time.time()

    data = request.get_json()
    text = data.get("text", "")

    if not text:
        return jsonify({"error": "text is required"}), 400

    key = generate_key(text)

    # 🔥 CHECK CACHE FIRST
    cached = get_cache(key)
    if cached:
        result = cached
    else:
        result = analyze_contract(text)
        set_cache(key, result)

    end = time.time()
    response_times.append(end - start)

    return jsonify({
        "analysis": result,
        "request_id": len(response_times)
    })


@contract_bp.route("/result/<int:req_id>", methods=["GET"])
def get_result(req_id):
    return jsonify({
        "analysis": "Analyzing contract risk completed.",
        "request_id": req_id
    })


# optional health helper data
def get_avg_response_time():
    if not response_times:
        return 0
    return sum(response_times) / len(response_times)
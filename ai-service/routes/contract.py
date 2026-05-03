from flask import Blueprint, request, jsonify
from services.groq_service import analyze_contract
from services.cache_service import get_cache, set_cache
from utils.hash_util import generate_key

from services.metrics_service import start_timer, end_timer

contract_bp = Blueprint("contract", __name__)


@contract_bp.route("/create", methods=["POST"])
def create_contract():
    start = start_timer()

    data = request.get_json()
    text = data.get("text", "")

    key = generate_key(text)

    cached = get_cache(key)
    if cached:
        result = cached
    else:
        result = analyze_contract(text)
        set_cache(key, result)

    end_timer(start)

    return jsonify({
        "analysis": result
    })
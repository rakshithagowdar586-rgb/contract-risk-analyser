from flask import Blueprint, request, jsonify
import hashlib
import time
from services.metrics_service import add_request_time
from services.cache_service import get_cache, set_cache
from services.groq_service import analyze_contract_safe


contract_bp = Blueprint("contract", __name__)


# ----------------------------
# SHA256 KEY
# ----------------------------
def generate_key(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


# ----------------------------
# RESPONSE TRACKING
# ----------------------------
request_times = []


def get_avg_response_time():
    if not request_times:
        return 0
    return sum(request_times) / len(request_times)



# ----------------------------
# MAIN ENDPOINT
# ----------------------------
@contract_bp.route("/create", methods=["POST"])
def create_contract():
    start = time.time()

    data = request.get_json()
    text = data.get("text", "")

    key = generate_key(text)

    # CACHE HIT
    cached = get_cache(key)
    if cached:
        rt = time.time() - start
        request_times.append(rt)

        return jsonify({
            "cached": True,
            "is_fallback": False,
            "response_time": round(rt, 4),
            "data": cached
        })
        

    # AI CALL
    result = analyze_contract_safe(text)

    set_cache(key, result["data"])

    rt = time.time() - start
    request_times.append(rt)
    add_request_time(rt)

    return jsonify({
        "cached": False,
        "is_fallback": result.get("is_fallback", False),
        "response_time": round(rt, 4),
        "data": result["data"]
    })
    
   
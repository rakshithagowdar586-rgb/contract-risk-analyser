from flask import Blueprint, request, jsonify
import hashlib, time
from services.cache_service import get_cache, set_cache
from services.metrics_service import add_request_time
from services.groq_service import analyze_contract_safe

contract_bp = Blueprint("contract", __name__)

def generate_key(text):
    return hashlib.sha256(text.encode("utf-8")).hexdigest()

@contract_bp.route("/create", methods=["POST"])
def create_contract():
    try:
        start = time.time()

        data = request.get_json(silent=True) or {}
        text = data.get("text")

        if not isinstance(text, str) or not text.strip():
            return jsonify({"error": "Invalid input: 'text' required"}), 400

        if len(text) > 5000:
            return jsonify({"error": "Text too large"}), 400

        key = generate_key(text)

        # CACHE
        cached = get_cache(key)
        if cached is not None:
            rt = time.time() - start
            add_request_time(rt)
            return jsonify({
                "cached": True,
                "is_fallback": False,
                "response_time": round(rt, 4),
                "data": cached
            }), 200

        # AI (SAFE)
        result = analyze_contract_safe(text) or {}

        data_block = result.get("data")
        if not isinstance(data_block, dict):
            data_block = {
                "title": "Fallback",
                "summary": "AI failed",
                "overview": "Fallback triggered",
                "key_items": [],
                "recommendations": []
            }
            result["is_fallback"] = True

        set_cache(key, data_block)

        rt = time.time() - start
        add_request_time(rt)

        return jsonify({
            "cached": False,
            "is_fallback": result.get("is_fallback", False),
            "response_time": round(rt, 4),
            "data": data_block
        }), 200

    except Exception as e:
        print(" ERROR in /create:", repr(e))
        return jsonify({"error": "Internal server error", "details": str(e)}), 500
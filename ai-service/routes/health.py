from flask import Blueprint, jsonify
from services.metrics_service import get_avg_response_time, get_uptime

health_bp = Blueprint("health", __name__)


@health_bp.route("/health", methods=["GET"])
def health():
    return jsonify({
        "model": "groq-llama",
        "avg_response_time": round(get_avg_response_time(), 4),
        "uptime": round(get_uptime(), 2)
    })
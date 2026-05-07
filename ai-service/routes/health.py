from flask import Blueprint, jsonify
from services.metrics_service import get_metrics, get_uptime

health_bp = Blueprint("health", __name__)

@health_bp.route("/health", methods=["GET"])
def health():
    metrics = get_metrics()

    # ALWAYS return JSON (never None)
    return jsonify({
        "status": "healthy",
        "model": "Groq-LLM / Contract Risk AI",
        "requests_tracked": metrics.get("requests_tracked", 0),
        "avg_response_time_sec": metrics.get("avg_response_time_sec", 0),
        "uptime_seconds": get_uptime()
    })
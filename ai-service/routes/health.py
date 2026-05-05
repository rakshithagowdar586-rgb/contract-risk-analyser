from flask import Blueprint, jsonify
from services.metrics_service import get_metrics, get_uptime

health_bp = Blueprint("health", __name__)

@health_bp.route("/health", methods=["GET"])
def health():
    metrics = get_metrics()

    return jsonify({
        "status": "healthy",
        "model": "Groq-LLM / Contract Risk AI",
        "uptime_seconds": get_uptime(),
        **metrics
    })
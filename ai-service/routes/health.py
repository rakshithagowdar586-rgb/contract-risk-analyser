from flask import Blueprint, jsonify
import time
import statistics

health_bp = Blueprint("health", __name__)

# store response times in memory
response_times = []

MODEL_NAME = "Groq-LLM / Contract Risk AI"

# middleware-like helper (called from other routes manually)
def start_timer():
    return time.time()

def end_timer(start):
    duration = time.time() - start
    response_times.append(duration)

    # keep only last 100 records
    if len(response_times) > 100:
        response_times.pop(0)

    return duration


@health_bp.route("/health", methods=["GET"])
def health():
    avg_time = statistics.mean(response_times) if response_times else 0

    return jsonify({
        "status": "healthy",
        "model": MODEL_NAME,
        "uptime_seconds": round(time.time() - time.process_time(), 2),
        "avg_response_time_sec": round(avg_time, 4),
        "requests_tracked": len(response_times)
    })
from flask import Flask, request, g
import time

from routes.contract import contract_bp
from routes.report import report_bp
from routes.health import health_bp

app = Flask(__name__)

app.register_blueprint(contract_bp)
app.register_blueprint(report_bp)
app.register_blueprint(health_bp)

# -----------------------------
# TIMER START
# -----------------------------
@app.before_request
def start_timer():
    g.start_time = time.time()


# -----------------------------
# AFTER REQUEST (COMBINED FIX)
# -----------------------------
@app.after_request
def add_headers_and_metrics(response):

    # Response time
    if hasattr(g, "start_time"):
        response_time = time.time() - g.start_time
        response.headers["X-Response-Time"] = str(round(response_time, 3))

    # Security headers (ZAP-ready)
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Content-Security-Policy"] = "default-src 'self'; object-src 'none'; frame-ancestors 'none'"
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"

    return response


if __name__ == "__main__":
    app.run(debug=False)
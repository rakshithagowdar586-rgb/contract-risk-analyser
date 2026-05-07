from flask import Flask, request, g
import time

# ----------------------------
# ROUTES (BLUEPRINTS)
# ----------------------------
from routes.contract import contract_bp
from routes.health import health_bp
from routes.report import report_bp

# ----------------------------
# MODEL LOADER
# ----------------------------
from services.model_loader import load_model

# ----------------------------
# APP INIT
# ----------------------------
app = Flask(__name__)
app.start_time = time.time()

# ----------------------------
# ROOT ROUTE
# ----------------------------
@app.route("/")
def home():
    return {
        "message": "Contract Risk AI API running",
        "status": "success"
    }

# ----------------------------
# REGISTER BLUEPRINTS
# ----------------------------
app.register_blueprint(contract_bp)
app.register_blueprint(health_bp)
app.register_blueprint(report_bp)

# ----------------------------
# REQUEST TIMER
# ----------------------------
@app.before_request
def start_timer():
    g.start_time = time.time()

# ----------------------------
# SECURITY + RESPONSE HEADERS
# ----------------------------
@app.after_request
def add_security_headers(response):

    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "DENY"
    response.headers["X-XSS-Protection"] = "1; mode=block"
    response.headers["Content-Security-Policy"] = "default-src 'self'"
    response.headers["Referrer-Policy"] = "no-referrer"
    response.headers["Permissions-Policy"] = "geolocation=(), microphone=(), camera=()"
    response.headers["Server"] = "SecureServer"

    if hasattr(g, "start_time"):
        response.headers["X-Response-Time"] = str(
            round(time.time() - g.start_time, 4)
        )

    return response

# ----------------------------
# MAIN
# ----------------------------
if __name__ == "__main__":
    print("Starting Contract Risk AI...")

    # preload model
    app = Flask(__name__)

    load_model()

    app.run(host="0.0.0.0", port=5000, debug=True)
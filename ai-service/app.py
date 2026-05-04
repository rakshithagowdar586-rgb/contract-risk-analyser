from flask import Flask
from routes.contract import contract_bp
from routes.report import report_bp
from routes.health import health_bp
import time

app = Flask(__name__)
app.start_time = time.time()

app.register_blueprint(contract_bp)
app.register_blueprint(report_bp)
app.register_blueprint(health_bp)

# ---------------- ZAP-READY SECURITY HEADERS ----------------
@app.after_request
def add_security_headers(response):
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
from flask import Flask
from routes.contract import contract_bp
from routes.health import health_bp
from routes.report import report_bp

from middleware.security_headers import add_security_headers

app = Flask(__name__)

app.register_blueprint(contract_bp)
app.register_blueprint(report_bp)
app.register_blueprint(health_bp)

# SECURITY HARDENING
app = add_security_headers(app)

if __name__ == "__main__":
    app.run(debug=False)
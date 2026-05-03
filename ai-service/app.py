from flask import Flask

from routes.contract import contract_bp
from routes.health import health_bp

app = Flask(__name__)

app.register_blueprint(contract_bp)
app.register_blueprint(health_bp)

if __name__ == "__main__":
    app.run(debug=True)
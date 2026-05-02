from flask import Flask
from routes.contract import contract_bp

app = Flask(__name__)

app.register_blueprint(contract_bp)

if __name__ == "__main__":
    app.run(debug=True)
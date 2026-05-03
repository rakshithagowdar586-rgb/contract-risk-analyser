from flask import Flask
from routes.contract import contract_bp

# Create Flask app
app = Flask(__name__)

# Register blueprint (IMPORTANT)
app.register_blueprint(contract_bp)

# Optional: test route (to check server running)
@app.route("/")
def home():
    return "AI Service is running 🚀"

# Run server
if __name__ == "__main__":
    app.run(debug=True, host="127.0.0.1", port=5000)
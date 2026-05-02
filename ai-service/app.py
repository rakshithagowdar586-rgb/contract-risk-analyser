from flask import Flask
from routes.describe import describe_bp
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)

app.register_blueprint(describe_bp)

@app.route("/")
def home():
    return {"message": "AI Service Running"}

if __name__ == "__main__":
    app.run(debug=True, port=5000)
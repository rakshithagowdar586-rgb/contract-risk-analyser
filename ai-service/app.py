from flask import Flask
from routes.describe import describe_bp

app = Flask(__name__)

# register routes
app.register_blueprint(describe_bp)

@app.route("/")
def home():
    return {"status": "AI Service Running"}

if __name__ == "__main__":
    app.run(debug=True)
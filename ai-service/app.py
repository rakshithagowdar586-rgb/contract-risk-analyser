from flask import Flask
from routes.describe import describe_bp
from routes.recommend import recommend_bp

app = Flask(__name__)

# Register routes
app.register_blueprint(describe_bp)
app.register_blueprint(recommend_bp)


# Health check (optional but useful)
@app.route("/")
def home():
    return {"message": "AI Contract Analyzer API is running"}


if __name__ == "__main__":
    app.run(debug=True)
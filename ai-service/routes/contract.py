from flask import Blueprint, request, jsonify
from services.model_loader import predict_risk

contract_bp = Blueprint("contract", __name__)


@contract_bp.route("/predict", methods=["POST"])
def predict():

    data = request.get_json()

    if not data or "text" not in data:
        return jsonify({
            "error": "Missing text"
        }), 400

    result = predict_risk(data["text"])

    return jsonify(result)
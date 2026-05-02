from flask import Blueprint, request, jsonify
from services.contract_service import ContractService

contract_bp = Blueprint("contract", __name__)

service = ContractService()

@contract_bp.route("/contract", methods=["POST"])
def create_contract():

    data = request.get_json()

    if "description" not in data:
        return jsonify({"error": "Missing description"}), 400

    result = service.create_contract(data)

    return jsonify({
        "status": "success",
        "contract": result
    })
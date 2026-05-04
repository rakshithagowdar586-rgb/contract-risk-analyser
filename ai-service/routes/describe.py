from flask import Blueprint, request, jsonify
from services.contract_service import ContractService
from services.groq_service import analyze_contract

describe_bp = Blueprint("describe", __name__)

service = ContractService()


@describe_bp.route("/describe", methods=["POST"])
def describe():

    print("\n===== /DESCRIBE HIT =====")

    data = request.json
    print("INPUT:", data)

    try:
        text = data.get("text")

        # STEP 1: CALL AI
        ai_result = analyze_contract(text)

        print("GROQ RESULT:", ai_result)

        # STEP 2: BUILD CONTRACT OBJECT
        contract = {
            "description": text,
            "aiAnalysis": ai_result
        }

        # STEP 3: PROCESS THROUGH SERVICE (IMPORTANT)
        processed = service.create_contract(contract)

        # STEP 4: RETURN FINAL CONTRACT
        return jsonify({
            "status": "success",
            "contract": processed
        })

    except Exception as e:
        print("ROUTE ERROR:", str(e))

        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
from flask import Blueprint, request, jsonify
from datetime import datetime
from services.groq_service import generate_recommendations
import json
import re

recommend_bp = Blueprint("recommend", __name__)

@recommend_bp.route("/recommend", methods=["POST"])
def recommend():
    try:
        data = request.get_json()

        # ✅ validation
        if not data or "text" not in data:
            return jsonify({
                "status": "error",
                "message": "Missing text"
            }), 400

        if not data["text"].strip():
            return jsonify({
                "status": "error",
                "message": "Empty text"
            }), 400

        raw_result = generate_recommendations(data["text"])

        # ✅ AI failure handling
        if not raw_result:
            return jsonify ({
                "status": "error",
                "message": "AI failed"
         }), 500

        # ✅ Extract JSON safely
        try:
            json_match = re.search(r"\{.*\}", raw_result, re.DOTALL)

            if not json_match:
                raise ValueError("No JSON found")

            parsed = json.loads(json_match.group())

        except Exception:
            return jsonify({
                "status": "error",
                "message": "Invalid AI response",
                "raw": raw_result
            }), 500

        recommendations = parsed.get("recommendations", [])

        # ✅ ensure 3 results
        if len(recommendations) != 3:
            return jsonify({
                "status": "error",
                "message": "AI did not return 3 recommendations",
                "raw": parsed
            }), 500

        return jsonify({
            "status": "success",
            "generated_at": datetime.utcnow().isoformat(),
            "recommendations": recommendations
        })

    except Exception as e:
        return jsonify({
            "status": "error",
            "message": str(e)
        }), 500
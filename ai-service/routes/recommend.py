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

        # ✅ Input validation
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

        # ✅ AI call
        raw_result = generate_recommendations(data["text"])

        # ✅ Extract JSON safely (fix for your error)
        try:
            # Find JSON block inside AI response
            json_match = re.search(r"\{.*\}", raw_result, re.DOTALL)

            if not json_match:
                raise ValueError("No JSON found")

            json_str = json_match.group()
            parsed = json.loads(json_str)

        except Exception:
            return jsonify({
                "status": "error",
                "message": "Invalid AI response",
                "raw": raw_result   # helpful for debugging
            }), 500

        # ✅ Extract recommendations
        recommendations = parsed.get("recommendations", [])

        # ✅ Ensure exactly 3 recommendations
        if len(recommendations) != 3:
            return jsonify({
                "status": "error",
                "message": "AI did not return exactly 3 recommendations",
                "raw": parsed
            }), 500

        # ✅ Final response
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
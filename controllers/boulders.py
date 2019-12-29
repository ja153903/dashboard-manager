from flask import request, jsonify, Blueprint
from models.boulders import Boulders


bouldering = Blueprint("bouldering", __name__)


@bouldering.route("/api/bouldering/stats", methods=["POST"])
def get_bouldering_stats():
    try:
        data = request.get_json()

        user_id = data["id"]

        user_bouldering_data = Boulders.query().filter_by(user_id=user_id).all()

        if not user_bouldering_data:
            raise Exception("No data for this user")

        return jsonify({"data": user_bouldering_data}), 200
    except Exception as e:
        return jsonify({"message": "No data for this user"}), 500


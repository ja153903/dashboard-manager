import uuid
from flask import request, jsonify, Blueprint
from models.authentication import Authentication

authentication = Blueprint("authentication", __name__)


@authentication.route("/api/login", methods=["POST"])
def authorize_login():
    try:
        data = request.get_json()

        email, password = data["email"], data["password"]

        is_authenticated = Authentication.query.filter_by(
            email=email, password=password
        ).first()

        if not is_authenticated:
            raise Exception("Returning None here")

        return jsonify({"validated": True, "token": str(uuid.uuid4())}), 200
    except Exception as e:
        return jsonify({"message": "You are not an authorized user"}), 500

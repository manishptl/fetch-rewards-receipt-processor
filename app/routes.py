from flask import request, jsonify
from services import process_receipt, calculate_reward_points
from utils import validate_receipt
from werkzeug.exceptions import BadRequest, NotFound

def routes_registration(app):
    @app.route("/", methods=["GET"])
    def home():
        return {
            "message": "Hello, Welcome to Receipt Processor & Rewards Calculator!",
            "add_receipt": "/receipts/process (POST)",
            "get_points": "/receipts/{id}/points (GET)"
        }

    @app.route("/receipts/process", methods=["POST"])
    def receipt_processor():
        receipt_data = request.get_json()

        is_valid, error_msg = validate_receipt(receipt_data)
        if not is_valid:
            raise BadRequest(description=error_msg)

        receipt_id = process_receipt(receipt_data)
        return jsonify({"id": receipt_id}), 201

    @app.route("/receipts/<receipt_id>/points", methods=["GET"])
    def get_points(receipt_id):
        points = calculate_reward_points(receipt_id)
        if points is None:
            raise NotFound(description="No receipt found for that ID.")

        return jsonify({"points": points}), 200

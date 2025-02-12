from flask import jsonify
from werkzeug.exceptions import BadRequest, NotFound, InternalServerError

def error_handler_registration(app):
    @app.errorhandler(BadRequest)
    def handle_bad_request(error):
        return jsonify({"error": error.description or "The receipt is invalid."}), 400

    @app.errorhandler(NotFound)
    def handle_not_found(error):
        return jsonify({"error": error.description or "Requested result not found."}), 404

    @app.errorhandler(InternalServerError)
    def handle_server_error(error):
        return jsonify({"error": "Internal Server Error"}), 500

from flask import Flask
from routes import routes_registration
from error_handlers import error_handler_registration

def create_application():
    app = Flask(__name__)
    routes_registration(app)
    error_handler_registration(app)
    return app

if __name__ == "__main__":
    app = create_application()
    app.run(host="0.0.0.0", port=5000)

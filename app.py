from flask import Flask
from src.controllers.login_manager import login_manager  # Importe o login_manager do módulo login_user
from src.routes.customer import customer_routes
from src.routes.contact import contact_routes
from src.routes.pages import pages
from src.routes.auth_routes import auth_routes
import os

app = Flask(__name__, template_folder='src/templates')
app.secret_key = os.getenv('SECRET_KEY')

def create_app():
    login_manager.init_app(app)

    # Registering the routes of the customer_routes blueprint
    app.register_blueprint(customer_routes)
    app.register_blueprint(contact_routes)
    app.register_blueprint(pages)
    app.register_blueprint(auth_routes)

    return app

app = create_app()

if __name__ == '__main__':
    app.run(port=5000, debug=True, ssl_context='adhoc')
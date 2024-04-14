from flask import Flask
from src.routes.customer import customer_routes

app = Flask(__name__)

# Registrando as rotas do blueprint customer_routes
app.register_blueprint(customer_routes)

if __name__ == '__main__':
    app.run(debug=True)
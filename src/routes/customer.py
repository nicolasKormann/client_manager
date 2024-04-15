from flask import Blueprint, request, jsonify
from infra.configs.connection import DBConnectionandler
from infra.repositories.customer_repository import CustomerRepository


customer_routes = Blueprint('customer_routes', __name__)
customer_repo = CustomerRepository(DBConnectionandler)



# Route to create a new customer
@customer_routes.route('/api/customers', methods=['POST'])
def create_customer():
    try:
        data = request.json
        full_name = data.get('full_name')
        email = data.get('email')
        phone = data.get('phone')
        response = customer_repo.create_customer(full_name, email, phone)
        return jsonify(response.serialize()), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500


# Route to get all customers
@customer_routes.route('/api/customers', methods=['GET'])
def get_all_customers():
    try:
        response = customer_repo.get_all_customers()
        return jsonify([customer.serialize() for customer in response])
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500


# Route to update a customer
@customer_routes.route('/api/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    try:
        data = request.json
        full_name = data.get('full_name')
        email = data.get('email')
        phone = data.get('phone')
        response = customer_repo.update_customer(customer_id, full_name, email, phone)
        return jsonify(response.serialize())
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500
    

# Route to delete a customer
@customer_routes.route('/api/customers/<int:customer_id>', methods=['DELETE'])
def delete_customer(customer_id):
    try:
        response = customer_repo.delete_customer(customer_id)        
        return jsonify(response.serialize())
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500

from flask import Blueprint, request, jsonify
from infra.configs.connection import DBConnectionandler
from infra.repositories.contact_repository import ContactRepository


contact_routes = Blueprint('contact_routes', __name__)
contact_repo = ContactRepository(DBConnectionandler)


# Route to create a new contact
@contact_routes.route('/api/contacts', methods=['POST'])
def create_contact():
    try:
        data = request.json
        full_name = data.get('full_name')
        email = data.get('email')
        phone = data.get('phone')
        customer_id = data.get('customer_id')
        response = contact_repo.create_contact(full_name, email, phone, customer_id)
        return jsonify(response.serialize()), 201
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500
    

# Route to get all contacts
@contact_routes.route('/api/contacts', methods=['GET'])
def get_all_contacts():
    try:
        response = contact_repo.get_all_contacts()
        return jsonify([contact.serialize() for contact in response])
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500
    
# Route to update a contact
@contact_routes.route('/api/contacts/<int:contact_id>', methods=['PUT'])
def update_contact(contact_id):
    try:
        data = request.json
        full_name = data.get('full_name')
        email = data.get('email')
        phone = data.get('phone')
        customer_id= data.get('customer_id')
        response = contact_repo.update_contact(contact_id, full_name, email, phone, customer_id)
        return jsonify(response.serialize())
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500
    
# Route to delete a contact
@contact_routes.route('/api/contacts/<int:contact_id>', methods=['DELETE'])
def delete_contact(contact_id):
    try:
        response = contact_repo.delete_contact(contact_id)
        return jsonify(response.serialize())
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500
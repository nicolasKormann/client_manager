from flask import Blueprint, request, jsonify
from infra.configs.connection import DBConnectionandler
from infra.repositories.customer_repository import CustomerRepository


report_route = Blueprint('report_route', __name__)
customer_repo = CustomerRepository(DBConnectionandler)

# Route to generate a customer report
@report_route.route('/api/report', methods=['GET'])
def generate_customer_report():
    try:
        response = customer_repo.generate_customer_report()
        return jsonify(response)
    except Exception as e:
        return jsonify({"error": f"An error occurred: {e}"}), 500
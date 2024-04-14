from infra.entities.customer import Customer


class CustomerRepository:

    def __init__(self, ConnectionHandler) -> None:
        self.__ConnectionHandler = ConnectionHandler
        self.__connection = self.__ConnectionHandler()


    def create_customer(self, full_name, email, phone):
        with self.__connection as conn:
            try:
                customer = Customer(full_name=full_name, email=email, phone=phone)
                conn.session.add(customer)
                conn.session.commit()
                conn.session.refresh(customer)
                return customer
            except Exception as exception:
                conn.session.rollback()
                raise exception 
            
    def get_all_customers(self):
        with self.__connection as conn:
            try:
                customers = conn.session.query(Customer).all()
                return [customer.serialize() for customer in customers]
            except Exception as exception:
                conn.session.rollback()
                raise exception
            
    def get_customer_by_id(self, customer_id):
        with self.__connection as conn:
            try:
                customer = conn.session.query(Customer).filter(Customer.id == customer_id).first()
                return customer
            except Exception as exception:
                conn.session.rollback()
                raise exception
            
    def update_customer(self, customer_id, full_name, email, phone):
        with self.__connection as conn:
            try:
                customer = conn.session.query(Customer).filter(Customer.id == customer_id).first()
                customer.full_name = full_name
                customer.email = email
                customer.phone = phone
                conn.session.commit()
                conn.session.refresh(customer)
                return customer
            except Exception as exception:
                conn.session.rollback()
                raise exception
            
    def delete_customer(self, customer_id):
        with self.__connection as conn:
            try:
                customer = conn.session.query(Customer).filter(Customer.id == customer_id).first()
                conn.session.delete(customer)
                conn.session.commit()
                return customer
            except Exception as exception:
                conn.session.rollback()
                raise exception
            
    def generate_customer_report(self):
        with self.__connection as conn:
            try:
                customers = conn.session.query(Customer).all()
                report_data = []
                for customer in customers:
                    customer_data = {
                        "customer_name": customer.full_name,
                        "contacts": []
                    }
                    for contact in customer.contacts:
                        contact_data = {
                            "full_name": contact.full_name,
                            "email": contact.email,
                            "phone": contact.phone
                        }
                        customer_data["contacts"].append(contact_data)
                    report_data.append(customer_data)
                return report_data
            except Exception as exception:
                conn.session.rollback()
                raise exception
                  

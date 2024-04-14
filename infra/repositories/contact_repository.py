from infra.entities.contact import Contact

class ContactRepository:
    def __init__(self, ConnectionHandler) -> None:
        self.__ConnectionHandler = ConnectionHandler
        self.__connection = self.__ConnectionHandler()

    def create_contact(self, full_name, email, phone, customer_id):
        with self.__connection as conn:
            try:
                contact = Contact(full_name=full_name, email=email, phone=phone, customer_id=customer_id)
                conn.session.add(contact)
                conn.session.commit()
                return contact
            except Exception as exception:
                conn.session.rollback()
                raise exception 
            
    def get_all_contacts(self):
        with self.__connection as conn:
            try:
                contacts = conn.session.query(Contact).all()
                return contacts
            except Exception as exception:
                conn.session.rollback()
                raise exception
            
    def get_contact_by_id(self, contact_id):
        with self.__connection as conn:
            try:
                contact = conn.session.query(Contact).filter(Contact.id == contact_id).first()
                return contact
            except Exception as exception:
                conn.session.rollback()
                raise exception
            
    def update_contact(self, contact_id, full_name, email, phone):
        with self.__connection as conn:
            try:
                contact = conn.session.query(Contact).filter(Contact.id == contact_id).first()
                contact.full_name = full_name
                contact.email = email
                contact.phone = phone
                conn.session.commit()
                return contact
            except Exception as exception:
                conn.session.rollback()
                raise exception
            
    def delete_contact(self, contact_id):
        with self.__connection as conn:
            try:
                contact = conn.session.query(Contact).filter(Contact.id == contact_id).first()
                conn.session.delete(contact)
                conn.session.commit()
            except Exception as exception:
                conn.session.rollback()
                raise exception
from infra.configs.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, ForeignKey, Column

class Contact(Base):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key=True)
    full_name = Column(String(100))
    email = Column(String(100))
    phone = Column(String(20))
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)

    customer = relationship("Customer", back_populates="contacts")

    def serialize(self):
        return {
            "id": self.id,
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone
        }
    
    def __repr__(self):
        return f"<Contact(full_name={self.full_name}, email={self.email}, phone={self.phone})>"
from infra.configs.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, Column, TIMESTAMP
from infra.entities.contact import Contact
import datetime


# Class that represents the customer entity
class Customer(Base):
    __tablename__ = "customer"

    id = Column(Integer, primary_key=True)
    full_name = Column(String(100))
    email = Column(String(100), unique=True)
    phone = Column(String(20))
    registration_date = Column(
        TIMESTAMP,
        default=datetime.datetime.now
    )

    contacts = relationship("Contact", back_populates="customer")

    def serialize(self):
        
        return {
            "id": self.id,
            "full_name": self.full_name,
            "email": self.email,
            "phone": self.phone,
            "registration_date": self.registration_date
        }

    def __repr__(self):
        return f"<Customer(full_name={self.full_name}, email={self.email}, phone={self.phone})>"
    

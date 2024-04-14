from infra.configs.base import Base
from sqlalchemy.orm import relationship
from sqlalchemy import Integer, String, ForeignKey, Column

class Contact(Base):
    __tablename__ = 'contact'

    id = Column(Integer, primary_key=True)
    full_name = Column(String(100))
    email = Column(String(100))
    phone = Column(String(20))
    customer_id = Column(Integer, ForeignKey('customer.id'))

    customer = relationship("Customer", back_populates="contacts")
from unittest import mock
from mock_alchemy.mocking import UnifiedAlchemyMagicMock
from infra.entities.customer import Customer
from infra.entities.contact import Contact
from infra.repositories.customer_repository import CustomerRepository


class ConnectionHandlerMock:
    def __init__(self) -> None:
        self.session = UnifiedAlchemyMagicMock(
            data = [
                (
                    [
                        mock.call.query(Customer),
                    ],
                    [
                        Customer(
                            full_name='John Doe', 
                            contacts=[
                                Contact(full_name='Contact 1', email='contact1@example.com', phone='1234567890'),
                                Contact(full_name='Contact 2', email='contact2@example.com', phone='0987654321')
                            ]
                        ), 
                        Customer(
                            full_name='Jane Smith', 
                            contacts=[
                                Contact(full_name='Contact 3', email='contact3@example.com', phone='1122334455')
                            ]
                        )
                    ],
                ),               
            ]
        )

    def __enter__(self):        
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()


def test_get_all_customers():
    customer_repository = CustomerRepository(ConnectionHandlerMock)
    response = customer_repository.get_all_customers()
    print()
    print(response)


def test_generate_customer_report():
    customer_repository = CustomerRepository(ConnectionHandlerMock)
    report_data = customer_repository.generate_customer_report()
    # Assert the expected report data
    assert len(report_data) == 2
    assert report_data[0]["customer_name"] == "John Doe"
    assert len(report_data[0]["contacts"]) == 2
    assert report_data[0]["contacts"][0]["full_name"] == "Contact 1"
    assert report_data[0]["contacts"][1]["full_name"] == "Contact 2"
    assert report_data[1]["customer_name"] == "Jane Smith"
    assert len(report_data[1]["contacts"]) == 1
    assert report_data[1]["contacts"][0]["full_name"] == "Contact 3"
    print()
    


       
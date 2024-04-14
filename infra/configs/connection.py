from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()


# Class to handle the connection with the database
class DBConnectionandler:

    def __init__(self) -> None:
        self.__connection_string = os.getenv('DB_URL')
        self.__engine = self.__create_database_engine()
        self.session = None

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine
    
    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()
        return self
    
    def __exit__(self, exc_type, exc_value, traceback):
        self.session.close()

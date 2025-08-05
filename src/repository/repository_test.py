import pytest
from src.models.connection.connection_handler import DBConnectionHandler
from .orders_repository import OrdersRepository

db_connection_handler = DBConnectionHandler()
db_connection_handler.connect_to_db()
conn = db_connection_handler.get_db_connection()


@pytest.mark.skip(reason="interação com o banco")
def test_insert_document():
    orders_repository = OrdersRepository(conn)
    my_doc = {"alguma": "coisaa", "valor": 5}

    orders_repository.insert_document(my_doc)


@pytest.mark.skip(reason="interação com o banco")
def test_insert_list_of_documents():
    orders_repository = OrdersRepository(conn)
    list_doc = [{"lista": 1}, {"lista": 2}]

    orders_repository.insert_list_of_documents(list_doc)

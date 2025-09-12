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

@pytest.mark.skip(reason="busca por varios elementos")
def test_select_many():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True}
    response =orders_repository.select_many(doc_filter)

    print()
    print(f"resposta do mongo: {response}")
    for doc in response:
        print(f"resposta dentro do for: {doc}")
        print()
        print(f"filtrando somente os itens: {doc['itens']}")

@pytest.mark.skip(reason="busca por um elemento")
def test_select_one():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"client": "Thiago Miziara"}
    response = orders_repository.select_one(doc_filter)

    print()
    print(f"resposta do mongo: {response}")

@pytest.mark.skip(reason="busca por propriedades específicas")
def test_select_many_with_properties():
    orders_repository = OrdersRepository(conn)
    doc_filter = {"cupom": True}
    response = orders_repository.select_many_with_properties(doc_filter)

    for doc in response:
        print(f"resposta dentro do for: {doc}")
        print()
        print(f"filtrando somente os itens: {doc['itens']}")

def test_select_if_property_exists():
    orders_repository = OrdersRepository(conn)
    response = orders_repository.select_if_property_exists()

    for doc in response:
        print(f"resposta dentro do for: {doc}")
        
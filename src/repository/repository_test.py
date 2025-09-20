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

@pytest.mark.skip(reason="busca por propriedades se existir")
def test_select_if_property_exists():
    orders_repository = OrdersRepository(conn)
    response = orders_repository.select_if_property_exists()

    for doc in response:
        print(f"resposta dentro do for: {doc}")


@pytest.mark.skip(reason="busca por propriedades específicas")
def test_select_many_with_multiple_filter():
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "cupom": True,
        "itens.doce": {"$exists": True}
    }
    response = orders_repository.select_many(doc_filter)

    for doc in response:
        print(doc)

@pytest.mark.skip(reason="busca por propriedades específicas")
def test_select_many_with_or_filter():
    orders_repository = OrdersRepository(conn)
    doc_filter = {
        "$or": [
            {"address": {"$exists": True}},
            {"itens.doce.tipo": "chocolate"}
        ]
    }
    response = orders_repository.select_many(doc_filter)

    for doc in response:
        print()
        print(doc)

@pytest.mark.skip(reason="busca por um documento específico")
def test_select_by_object_id():
    orders_repository = OrdersRepository(conn)
    doc_id = "68bb1ed571594250a6b80cb8"
    response = orders_repository.select_by_object_id(doc_id)

    print()
    print(f"resposta do mongo: {response}")

@pytest.mark.skip(reason="edição de um documento específico")
def test_edit_register():
    orders_repository = OrdersRepository(conn)
    doc_id = "68bb1ed571594250a6b80cb8"
    updated_data = {
        "client": "Thiago Miziara - editado",
        "cupom": True,
        "itens.pizza.quantidade": 2
    }
    orders_repository.edit_register(doc_id, updated_data)

@pytest.mark.skip(reason="edição de varios registros")
def test_edit_many_registers():
    orders_repository = OrdersRepository(conn)
    updated_data = {
        "itens.refrigerante.tipo": "fanta"
    }
    doc_filter = {"itens.refrigerante": {"$exists": True}}

    orders_repository.edit_many_registers(updated_data, doc_filter)

@pytest.mark.skip(reason="edição de um registro específico")
def test_edit_register_with_increment():
    orders_repository = OrdersRepository(conn)
    doc_id = "68bb1ed571594250a6b80cb8"
    update_data = {
        "itens.pizza.quantidade": 1
    }
    orders_repository.edit_register_with_increment(doc_id, update_data)

def test_edit_register_with_decrement():
    orders_repository = OrdersRepository(conn)
    doc_id = "68bb1ed571594250a6b80cb8"
    update_data = {
        "itens.pizza.quantidade": -11
    }
    orders_repository.edit_register_with_decrement(doc_id, update_data)
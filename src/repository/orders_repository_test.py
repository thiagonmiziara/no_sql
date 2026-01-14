from .orders_repository import OrdersRepository

class CollectionMock:
    def __init__(self):
        self.insert_one_attributes = {}
        self.find_attributes = {}

    def insert_one(self, input_data: any) -> None:
        self.insert_one_attributes["dict"] = input_data

    def find(self, *args):
        self.find_attributes['args'] = args


class DBConnectionHandlerMock:
    def __init__(self, colection):
        self.colection = colection
        self.get_collection_attributes = {}

    def get_collection(self, collection_name):
        self.get_collection_attributes["collection_name"] = collection_name
        return self.colection


def test_insert_document():
    collection_mock = CollectionMock()
    db_connection_handler_mock = DBConnectionHandlerMock(collection_mock)
    orders_repository = OrdersRepository(db_connection_handler_mock)
    my_doc = {"alguma": "coisaa", "valor": 5}

    orders_repository.insert_document(my_doc)

    assert db_connection_handler_mock.get_collection_attributes["collection_name"] == "orders"
    assert collection_mock.insert_one_attributes["dict"] == my_doc


def test_select_many_with_properties():
    collection_mock = CollectionMock()
    db_connection_handler_mock = DBConnectionHandlerMock(collection_mock)
    orders_repository = OrdersRepository(db_connection_handler_mock)
    doc_filter = {"cupom": True}

    orders_repository.select_many_with_properties(doc_filter)

    assert db_connection_handler_mock.get_collection_attributes["collection_name"] == "orders"
    assert collection_mock.find_attributes['args'][0] == doc_filter
    assert collection_mock.find_attributes['args'][1] == {
        "_id": 0,
        "cupom": 0,
    }


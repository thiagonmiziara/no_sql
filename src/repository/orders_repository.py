from bson.objectid import ObjectId

class OrdersRepository:
    def __init__(self, db_connection) -> None:
        self.__collection_name = "orders"
        self.__db_connection = db_connection

    def insert_document(self, document: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_one(document)

    def insert_list_of_documents(self, list_of_documents: list) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.insert_many(list_of_documents)

    def select_many(self,doc_filter:dict) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(doc_filter)
        return data
    
    def select_one(self,doc_filter:dict) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one(doc_filter)
        return response
    
    def select_many_with_properties(self, doc_filter:dict) -> list:
        collection = self.__db_connection.get_collection(self.__collection_name)
        data = collection.find(
            doc_filter,
            {
                "_id": 0,
                "cupom": 0,
            } # remove these properties from the result,
        )
        return data
    
    def select_if_property_exists(self) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find(
            {"address": {"$exists": True}},
            {"_id": 0, "address": 1}
        )
        return response

    def select_by_object_id(self, doc_id: str) -> dict:
        collection = self.__db_connection.get_collection(self.__collection_name)
        response = collection.find_one({"_id": ObjectId(doc_id)})
        return response

    def edit_register(self, doc_id: str, updated_data: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            {"_id": ObjectId(doc_id)},
            {"$set": updated_data}
        )

    def edit_many_registers(self, updated_data: dict, doc_filter: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_many(
            doc_filter,
            {"$set": updated_data}
        )

    def edit_register_with_increment(self, doc_id:str, update_data:dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            {"_id": ObjectId(doc_id)},
            {"$inc": update_data}
        )

    def edit_register_with_decrement(self, doc_id:str, update_data:dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.update_one(
            {"_id": ObjectId(doc_id)},
            {"$inc": update_data}
        )

    def delete_register(self, doc_id: str) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_one({"_id": ObjectId(doc_id)})

    def delete_many_registers(self, doc_filter: dict) -> None:
        collection = self.__db_connection.get_collection(self.__collection_name)
        collection.delete_many(doc_filter)
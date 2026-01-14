from abc import  ABC, abstractmethod


class OrdersRepositoryInterface(ABC):
    @abstractmethod
    def insert_document(self, document: dict) -> None:
      pass

    @abstractmethod
    def insert_list_passof_documents(self, list_of_documents: list) -> None:
      pass

    @abstractmethod
    def select_many(self,doc_filter:dict) -> list:
      pass

    @abstractmethod
    def select_one(self,doc_filter:dict) -> dict:
      pass

    @abstractmethod
    def select_many_with_properties(self, doc_filter:dict) -> list:
      pass

    @abstractmethod
    def select_if_property_exists(self) -> dict:
      pass

    @abstractmethod
    def select_by_object_id(self, doc_id: str) -> dict:
      pass

    @abstractmethod
    def edit_register(self, doc_id: str, updated_data: dict) -> None:
      pass

    @abstractmethod
    def edit_many_registers(self, updated_data: dict, doc_filter: dict) -> None:
      pass

    @abstractmethod
    def edit_register_with_increment(self, doc_id:str, update_data:dict) -> None:
      pass

    @abstractmethod
    def edit_register_with_decrement(self, doc_id:str, update_data:dict) -> None:
      pass

    @abstractmethod
    def delete_register(self, doc_id: str) -> None:
      pass

    @abstractmethod
    def delete_many_registers(self, doc_filter: dict) -> None:
      pass


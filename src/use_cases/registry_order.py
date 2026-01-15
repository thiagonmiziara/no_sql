from datetime import datetime
from src.models.repository.interfaces.orders_repository import OrdersRepositoryInterface
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

class RegistryOrderUseCase:
    def __init__(self, orders_repository: OrdersRepositoryInterface) -> None:
        self.__orders_repository = orders_repository

    def registry(self, http_request: HttpRequest) -> HttpResponse:
        try:
            order_data = http_request.body
            new_order = self.__format_new_order(order_data)
            self.__registry_order(new_order)

            return self.__format_response()
        except Exception as exception:
            return HttpResponse(status_code=400, body={
                "error": str(exception)
            })


    def __format_new_order(self, order_data: dict) -> dict:
        new_order = order_data["data"]
        formatted_order ={**new_order, "created_at": datetime.now()}
        return formatted_order

    def __registry_order(self, new_order: dict) -> None:
        self.__orders_repository.insert_document(new_order)


    def __format_response(self) -> dict:
        return HttpResponse(status_code=201, body={
            "data": {
                "type": "order",
                "count": 1,
                "registry": True
            }
        })

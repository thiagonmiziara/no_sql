from flask import Blueprint, request, jsonify
from src.main.http_types.http_request import HttpRequest
from src.main.http_types.http_response import HttpResponse

delivery_routes_bp = Blueprint('delivery_routes', __name__)

@delivery_routes_bp.route('/delivery/order', methods=['POST'])
def register_order():
    data = request.get_json()
    http_request = HttpRequest(
        method=request.method,
        url=request.url,
        headers=dict(request.headers),
        body=data
    )

    http_response = HttpResponse(
        status_code=201,
        body={"message": "Order registered successfully"}
    )

    return jsonify(http_response.body), http_response.status_code

from flask import Blueprint, request, jsonify

delivery_routes_bp = Blueprint('delivery_routes', __name__)

@delivery_routes_bp.route('/delivery/order', methods=['POST'])
def register_order():
    data = request.get_json()
    print(data)
    # Logic to register a delivery order
    return jsonify({"message": "Order registered successfully", "data": data}), 201

from flask import abort, jsonify
from flask_restful import Resource

from carford.models import Car, Order


class CarResource(Resource):
    def get(self):
        cars = Car.query.all() or abort(204)
        return jsonify(
            {"cars": [car.to_dict() for car in cars]}
        )


class CarItemResource(Resource):
    def get(self, car_id):
        car = Car.query.filter_by(id=car_id).first() or abort(404)
        return jsonify(car.to_dict())
    
    
class OrderResource(Resource):
    def get(self):
        orders = Order.query.all() or abort(204)
        return jsonify(
            {"orders": [order.to_dict() for order in orders]}
        )
        

class OrderItemResource(Resource):
    def get(self, order_id):
        order = Order.query.filter_by(id=order_id).first() or abort(404)
        return jsonify(order.to_dict())

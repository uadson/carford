from flask import abort, render_template
from carford.models import Car, Order, User


def index():
    # cars = Car.query.all()
    orders = Order.query.all()
    return render_template("index.html", orders=orders)


def car(car_id):
    car = Car.query.filter_by(id=car_id).first() or abort(
        404, "car not found"
    )
    return render_template("car.html", car=car)


def order(order_id):
    order = Order.query.filter_by(id=order_id).first() or abort (
        404, "order not found"
    )
    user = User.query.filter_by(id=order.user_id).first()
    car = Car.query.filter_by(id=order.car_id).first()
    return render_template("order.html", order=order, user=user, car=car)
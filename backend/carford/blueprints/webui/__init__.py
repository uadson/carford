from flask import Blueprint

from .views import index, car, order

bp = Blueprint("webui", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=index)
bp.add_url_rule(
    "/car/<car_id>", view_func=car, endpoint="carview"
)
bp.add_url_rule(
    "/order/<order_id>", view_func=order, endpoint="orderview"
)

def init_app(app):
    app.register_blueprint(bp)

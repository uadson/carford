from carford.ext.database import db
from sqlalchemy_serializer import SerializerMixin


class Car(db.Model, SerializerMixin):
    __tablename__ = "cars"
    
    id = db.Column(db.Integer, primary_key=True)
    color = db.Column(db.String(10))
    model = db.Column(db.String(20))


class User(db.Model, SerializerMixin):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(140))
    password = db.Column(db.String(512))
    

class Order(db.Model, SerializerMixin):
    __tablename__ = "orders"
    
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    car_id = db.Column(db.Integer, db.ForeignKey("cars.id"))
    
    user = db.relationship("User", foreign_keys=user_id)
    car = db.relationship("Car", foreign_keys=car_id)
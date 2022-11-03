import click
from carford.ext.database import db
from carford.ext.auth import create_user
from carford.models import Car, Order


def create_db():
    """Creates database"""
    db.create_all()


def drop_db():
    """Cleans database"""
    db.drop_all()


def populate_db():
    """Populate db with sample data"""
    data = [
        Car(id=1, color="yellow", model="hatch"),
        Car(id=2, color="blue", model="sedan"),
        Car(id=3, color="grey", model="convertible"),
        Order(id=1, user_id=1, car_id=1),
        Order(id=2, user_id=2, car_id=2),
        Order(id=3, user_id=3, car_id=3),
    ]
    db.session.bulk_save_objects(data)
    db.session.commit()
    return Car.query.all()


def init_app(app):
    # add multiple commands in a bulk
    for command in [create_db, drop_db, populate_db]:
        app.cli.add_command(app.cli.command()(command))

    # add a single command
    @app.cli.command()
    @click.option('--username', '-u')
    @click.option('--password', '-p')
    def add_user(username, password):
        """Adds a new user to the database"""
        return create_user(username, password)

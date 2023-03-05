from flask import Flask
import sqlite3
from flask_sqlalchemy import SQLAlchemy, session
from timestamp_creation import timestamps_int
from coordinate_creation import create_coordinates

app = Flask(__name__)

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///coordinate-collection.db"
db.init_app(app)


# creating a database for drone coordinates and timestamps
class Coordinates(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    epoch_time = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.id


# initializing database
# with app.app_context():
#     db.create_all()


def create_database():
    for i in range(len(timestamps_int)):
        with app.app_context():
            coordinate = Coordinates(
                        latitude=create_coordinates()[0],
                        longitude=create_coordinates()[1],
                        epoch_time=timestamps_int[i],
                    )
            db.session.add(coordinate)
            db.session.commit()


def database_to_list():
    with app.app_context():
        return db.session.query(Coordinates).all()

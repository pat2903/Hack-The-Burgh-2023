from flask import Flask
import sqlite3
from flask_sqlalchemy import SQLAlchemy
import random

app = Flask(__name__)

db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///coordinate-collection.db"
db.init_app(app)


class Coordinates(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    epoch_time = db.Column(db.Integer, nullable=False)


# with app.app_context():
#     db.create_all()

with open("timestamps.txt") as file:
    times = file.readlines()
    times_int = []
    for time in times:
        times_int.append(int(time))

for i in range(len(times_int)):
    rand_lat = round(30 + random.random() * 13, 3)
    rand_long = round(81 + random.random() * 36, 3)
    with app.app_context():
        coordinate = Coordinates(
                    latitude=rand_lat,
                    longitude=rand_long,
                    epoch_time=times_int[i],
                )
        db.session.add(coordinate)
        db.session.commit()

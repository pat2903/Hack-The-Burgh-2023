from flask import Flask, jsonify, render_template
from flask_cors import CORS
from database_inspection import select_coordinates

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route("/")
def home():
    return jsonify("Hello World")


@app.route("/get-coordinates")
def get_coordinates():
    coordinates_list = select_coordinates()
    json_objects = []
    for coordinate in coordinates_list:
        json_data = {
            "latitude": coordinate["latitude"],
            "longitude": coordinate["longitude"],
            "timestamp": coordinate["timestamp"]
        }
        json_objects.append(json_data)
    return jsonify(json_objects)


if __name__ == "__main__":
    app.run(debug=True)

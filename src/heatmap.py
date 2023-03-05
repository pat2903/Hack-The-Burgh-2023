from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    pass


@app.route("/get-coordinates")
def get_coordinates():
    pass


if __name__ == "__main__":
    app.run(debug=True)
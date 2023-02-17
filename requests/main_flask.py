__winc_id__ = "cc1b724762854e85a8defa04287f708b"
__human_name__ = "requests"

from flask import Flask

# Eerste stappen met Flask

# app = Flask(__name__)

# @app.route("/")
# def hello_world():
#    return "<p>Hello, World!</p>"

# route in cmd
# cd desktop cd hello-world cd requests
# set FLASK_APP=main_flask.py
# flask run

app = Flask(__name__)

@app.route("/")
def home_sweet_home():
    return "<p>Home, sweet home.</p>"


@app.route("/greet")
def greet():
    return "<h1>Hello, world!</h1>"


@app.route("/greet/<example_name>")
def greet_name(example_name= None):
    if example_name == "<example_name>":
        return "<h1>Hello, you beautiful person!</h1>"
    else:
        return f"<h1>Hello, {example_name}!</h1>"


if __name__ == '__main__':
    app.run(debug=True)


# cmd: python main_flask.py
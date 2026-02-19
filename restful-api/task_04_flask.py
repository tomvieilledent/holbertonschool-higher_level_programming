#!/usr/bin/python3

from flask import Flask, jsonify

app = Flask(__name__)

users = {
    "jane": {
        "username": "jane",
        "name": "Jane",
        "age": 28,
        "city": "Los Angeles"
    },
    "john": {
        "username": "john",
        "name": "John",
        "age": 30,
        "city": "New York"
    }
}


@app.route('/')
def home():
    return 'Welcome to the Flask API!'


@app.route('/data')
def data():
    return jsonify(users)


@app.route('/status')
def status():
    return ('OK')


@app.route("/users/<username>")
def username(username):
    if username in users:
        return users[username], 200
    else:
        return {"error": "User not found"}, 404


if __name__ == "__main__":
    app.run()

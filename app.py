#!/usr/bin/python3

#flask hello world

from flask import Flask

app = Flask(__name__)

#decorator pattern
@app.route("/")
@app.route("/hello")

#define the view

def hello_world():
    return "hello, world"

#start the dev server using the run() method
if __name__ == "__main__":
    app.run()


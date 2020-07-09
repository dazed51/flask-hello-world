#!/usr/bin/python3

#flask hello world

from flask import Flask

app = Flask(__name__)

#error handling
app.config["DEBUG"] = True

#decorator pattern
@app.route("/")
@app.route("/hello")

#define the view

def hello_world():
    return "hello, world!?!?!?!"

#dynamic route
@app.route("/test/<search_query>")
def search(search_query):
    return search_query

#dynamic route with explict status codes
@app.route("/name/<name>")
def index(name):
   if name.lower() == "mike" :
       return "hello, {}".format(name)
   else :
       return "not found", 404

#start the dev server using the run() method
if __name__ == "__main__":
    app.run()


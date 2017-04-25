from flask import Flask
from flask import request

from query import *

player1 = Player()
my_map = Map()

app = Flask(__name__)

@app.route("/")
def home():
    return "Looks like you're lost, friend!"

@app.route("/q/<q>")
def text_query(q):
    #return query.parse_query(q, None, None, None)
    return game(player1, my_map)

@app.route("/q", methods=["POST"])
def text_query_post():
    query_text = request.form["q"]
    location = request.form["l"]
    timestamp = request.form["t"]
    session_token = request.form["session_token"]
    return game(player1, my_map)
    #return query.parse_query(query_text, location, timestamp, session_token)

@app.route("/vq", methods=["POST"])
def voice_query_post():
    return game(player1, my_map)
    #return query.parse_voice(request.form)

if __name__ == '__main__':
    app.run()

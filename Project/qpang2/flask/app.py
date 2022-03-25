from flask import Flask, render_template
import requests
import json

app = Flask(__name__)
@app.route("/")
def home():
    return "home"


@app.route("/restaurant")
def rest():
    r = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=Chinese&location=40.110740,-88.219940&language=en&radius=500&sensor=false&key=AIzaSyBwQIJgd3BTxyNA8ccg6vcplWGA5kWNbNE&types=restaurant")
    res = r.text
    data = json.loads(res)
    return data
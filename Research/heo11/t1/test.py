from flask import Flask, redirect, render_template, request
import requests
import json

app = Flask(__name__)

API_KEY = "AIzaSyBwQIJgd3BTxyNA8ccg6vcplWGA5kWNbNE"

@app.route("/getDirectionTime", methods=["POST"])
def getDirection(currentLoc, destLoc):
    url = "https://maps.googleapis.com/maps/api/directions/json?"
    r = requests.get(url + "origin=" + currentLoc + "&destination=place_id:" + destLoc + "&key=" + API_KEY)
    directions = json.loads(r)
    return directions

def getDirection(currentLoc, destLoc):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"
    r = requests.get(url + "origin=" + currentLoc + "&destination=place_id:" + destLoc + "&key=" + API_KEY)
    time = r.json()["rows"][0]["elements"][0]["duration"]["text"]
    seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]
    
    return "\n Total duration will be around", time

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
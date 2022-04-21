from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

API_KEY = "AIzaSyBwQIJgd3BTxyNA8ccg6vcplWGA5kWNbNE"

def getTimeDuration(currentLoc, destLoc, mode = "walking"):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"
    r = requests.get(url + "origins=" + currentLoc + "&destinations=" + destLoc + "&mode=" + mode + "&key=" + API_KEY)
    data = json.loads(r.text)
    return str(data["rows"][0]["elements"][0]["duration"]["value"])
    
def getTimeDurationOnFront(currentLoc, destLoc, mode = "walking"):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"
    r = requests.get(url + "origin=" + currentLoc + "&destination=place_id:" + destLoc + "&mode=" + mode + "&key=" + API_KEY)
    time = r.json()["rows"][0]["elements"][0]["duration"]["text"]
    seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]
    return "\n Total duration will be around", time

def timefilter(reslist, currentLoc, destLoc, eatingtime, startingtime, endtime, mode = "walking"):
    filtered = []
    duration = endtime - startingtime
    for res in reslist:
        totaltime = (int(getTimeDuration(currentLoc, "place_id:" + res["place_id"])) + int(getTimeDuration("place_id:" + res["place_id"],destLoc))) / 60 + eatingtime 
        if totaltime < duration:
            filtered.append(res)
    return filtered


def operationfilter(reslist):
    filtered = []
    for res in reslist:
        if res["business_status"] == "OPERATIONAL":
            filtered.append(res)
    return filtered

def openingfilter(reslist):
    filtered = []
    for res in reslist:
        if res["opening_hours"]["open_now"] == True:
            filtered.append(res)
    return filtered

def higherpricefilter(reslist,pricelevel):
    filtered = []
    for res in reslist:
        if res["price_level"] >= pricelevel:
            filtered.append(res)
    return filtered


def lowerpricefilter(reslist,pricelevel):
    filtered = []
    for res in reslist:
        if res["price_level"] <= pricelevel:
            filtered.append(res)
    return filtered

def ratingfilter(reslist,rating):
    filtered = []
    for res in reslist:
        if res["rating"] >= rating:
            filtered.append(res)
    return filtered

def placeID(reslist):
    IDs = []
    for res in reslist:
        IDs.append(res.place_id + ":" + res.name)
    return IDs

def request(body):
    if "keyword" not in body.keys:
        r = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=40.110740,-88.219940&language=en&radius=" + str(body["radius"]) + "&sensor=false&key=AIzaSyBwQIJgd3BTxyNA8ccg6vcplWGA5kWNbNE&types=restaurant")
    else:
        r = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=" + body["keyword"] + "&location=40.110740,-88.219940&language=en&radius=" + str(body["radius"]) + "&sensor=false&key=AIzaSyBwQIJgd3BTxyNA8ccg6vcplWGA5kWNbNE&types=restaurant")
    res = r.text
    data = json.loads(res)
    reslist = []
    for res in data["results"]:
        reslist.append(res)
    return reslist

def requesttest():
    r = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=40.110740,-88.219940&language=en&radius=" + "1000" + "&sensor=false&key=AIzaSyBwQIJgd3BTxyNA8ccg6vcplWGA5kWNbNE&types=restaurant")
    res = r.text
    data = json.loads(res)
    reslist = []
    for res in data["results"]:
        reslist.append(res)
    return reslist

@app.route("/")
def home():
    return getTimeDuration("1301%W%Springfield%Ave%Urbana%IL", "603%S%Wright%St%Champaign%IL")

@app.route("/restaurant")
def rest():
    return str(timefilter(requesttest(),"1301%W%Springfield%Ave%Urbana%IL", "603%S%Wright%St%Champaign%IL", 15, 50, 90))

@app.route("/restaurant/rating/<rating>")
def rate(rating):
    return ratingfilter(request(),float(rating))
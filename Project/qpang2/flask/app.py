from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def operationfilter(dict):
    filtered = {}
    for res in dict["results"]:
        if res["business_status"] == "OPERATIONAL":
            filtered[res["name"]] = res
    return filtered

def openingfilter(dict):
    filtered = {}
    for res in dict["results"]:
        if res["opening_hours"]["open_now"] == True:
            filtered[res["name"]] = res
    return filtered

def higherpricefilter(dict,pricelevel):
    filtered = {}
    for res in dict["results"]:
        if res["price_level"] >= pricelevel:
            filtered[res["name"]] = res
    return filtered


def lowerpricefilter(dict,pricelevel):
    filtered = {}
    for res in dict["results"]:
        if res["price_level"] <= pricelevel:
            filtered[res["name"]] = res
    return filtered

def ratingfilter(dict,rating):
    filtered = {}
    for res in dict["results"]:
        if res["rating"] >= rating:
            filtered[res["name"]] = res
    return filtered

def placeID(dict,rating):
    IDs = {}
    for res in dict["results"]:
        IDs[res["name"]] = res["place_id"]
    return IDs

def request(keyword="none",radius=1000):
    if keyword == "none":
        r = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=40.110740,-88.219940&language=en&radius=" + str(radius) + "&sensor=false&key=AIzaSyBwQIJgd3BTxyNA8ccg6vcplWGA5kWNbNE&types=restaurant")
    else:
        r = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=" + keyword + "&location=40.110740,-88.219940&language=en&radius=" + str(radius) + "&sensor=false&key=AIzaSyBwQIJgd3BTxyNA8ccg6vcplWGA5kWNbNE&types=restaurant")
    res = r.text
    data = json.loads(res)
    return data

@app.route("/")
def home():
    return "home"

@app.route("/restaurant")
def rest():
    return request()

@app.route("/restaurant/<kw>")
def keysearch(kw):
    return ratingfilter(request(keyword=kw),4.0)

@app.route("/restaurant/rating/<rating>")
def rate(rating):
    return ratingfilter(request(),float(rating))
from random import normalvariate
from flask import Flask, render_template, jsonify, make_response, request
import requests
import json

app = Flask(__name__)

API_KEY = "AIzaSyBwQIJgd3BTxyNA8ccg6vcplWGA5kWNbNE"

def getTimeDuration(currentLoc, destLoc, mode = "walking"):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"
    r = requests.get(url + "origins=" + currentLoc + "&destinations=" + destLoc + "&mode=" + mode + "&key=" + API_KEY)
    data = json.loads(r.text)
    return str(data["rows"][0]["elements"][0]["duration"]["value"])

# options to fileters are listed 
# called after the data is received and casted from request

def timefilter(reslist, currentLoc, destLoc, eatingtime, startingtime, endtime, mode = "walking"):
    filtered = []
    duration = int(endtime) - int(startingtime)
    for res in reslist:
        firsttime = int(getTimeDuration(currentLoc, "place_id:" + res["place_id"])) /60
        secondtime = int(getTimeDuration("place_id:" + res["place_id"],destLoc)) /60
        totaltime =  firsttime + secondtime + int(eatingtime)
        if totaltime < duration:
            res["ToResTime"] = firsttime
            res["ToDesTime"] = secondtime
            res["TotalTime"] = totaltime
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

# unique PlaceID generatings

def placeID(reslist):
    IDs = []
    for res in reslist:
        IDs.append(res.place_id + ":" + res.name)
    return IDs

# sort functions are lisdted
# called after options are filtered, for display

# general sort for all

def sortByName(reslist):
    sortedJson = sorted(reslist, key=lambda x: x["name"])
    return sortedJson

def sortByNameReverse(reslist):
    sortedJson = sorted(reslist, key=lambda x: x["name"], reverse=True)
    return sortedJson

def sortByPrice(reslist):
    noPriceLev = []
    copy = reslist
    for res in reslist:
        if "price_level" not in res:
            noPriceLev.append(res)
            copy.remove(res)
            
    copy = sortByName(copy)
    sortedJson = sorted(copy, key=lambda x: x['price_level'])
    sortedJson += noPriceLev
    return sortedJson

def sortByPriceReverse(reslist):
    noPriceLev = []
    copy = reslist
    for res in reslist:
        if "price_level" not in res:
            noPriceLev.append(res)
            copy.remove(res)
            
    copy = sortByName(copy)
    sortedJson = sorted(copy, key=lambda x: x['price_level'], reverse=True)
    sortedJson += noPriceLev
    return sortedJson

def sortByRate(reslist):
    noRate = []
    copy = reslist
    for res in reslist:
        if "rating" not in res:
            noRate.append(res)
            copy.remove(res)

    copy = sortByName(copy)
    sortedJson = sorted(copy, key=lambda x: x['rating'], reverse=True)
    sortedJson += noRate
    return sortedJson

def sortByRateReverse(reslist):
    noRate = []
    copy = reslist
    for res in reslist:
        if "rating" not in res:
            noRate.append(res)
            copy.remove(res)

    copy = sortByName(copy)
    sortedJson = sorted(copy, key=lambda x: x['rating'])
    sortedJson += noRate
    return sortedJson

def sortByTime(reslist):
    reslist = sortByName(reslist)
    sortedJson = sorted(reslist, key=lambda x: x['TotalTime'])
    return sortedJson

def sortByTimeReverse(reslist):
    reslist = sortByName(reslist)
    sortedJson = sorted(reslist, key=lambda x: x['TotalTime'], reverse=True)
    return sortedJson

# main

def respondRequest(body):
    if "keyword" not in body:
        r = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=40.110740,-88.219940&language=en&radius=" + str(body["radius"]) + "&sensor=false&key=AIzaSyBwQIJgd3BTxyNA8ccg6vcplWGA5kWNbNE&types=restaurant")
    else:
        r = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=" + body["keyword"] + "&location=40.110740,-88.219940&language=en&radius=" + str(body["radius"]) + "&sensor=false&key=AIzaSyBwQIJgd3BTxyNA8ccg6vcplWGA5kWNbNE&types=restaurant")
    res = r.text
    data = json.loads(res)
    reslist = []
    for res in data["results"]:
        reslist.append(res)
    if "opening" in body:
        reslist = openingfilter(reslist)
    if "rating" in body:
        reslist = ratingfilter(reslist, float(body["rating"]))
    if "lowerprice" in body:
        reslist = lowerpricefilter(reslist, float(body["lowerprice"]))
    if "higherprice" in body:
        reslist = higherpricefilter(reslist, float(body["higherprice"]))
    if "timeinfo" in body:
        reslist = timefilter(reslist, body["timeinfo"]["currentloc"], body["timeinfo"]["destloc"], body["timeinfo"]["eatingtime"], body["timeinfo"]["starttime"], body["timeinfo"]["endtime"])
    if "sortby" in body:
        if body["sortby"] == "name":
            reslist = sortByName(reslist)
        if body["sortby"] == "HighPrice":
            reslist = sortByPrice(reslist)
        if body["sortby"] == "LowPrice":
            reslist = sortByPriceReverse(reslist)
        if body["sortby"] == "HighRate":
            reslist = sortByRate(reslist)
        if body["sortby"] == "LowRate":
            reslist = sortByRateReverse(reslist)
    return reslist

def requesttest():
    r = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=40.110740,-88.219940&language=en&radius=" + "2000" + "&sensor=false&key=AIzaSyBwQIJgd3BTxyNA8ccg6vcplWGA5kWNbNE&types=restaurant")
    res = r.text
    data = json.loads(res)
    reslist = []
    for res in data["results"]:
        reslist.append(res)
    return reslist

@app.route("/")
def home():
    return str(sortByRate(requesttest()))

@app.route("/restaurant", methods=['POST'])
def rest():
    data = request.get_json()
    print(data)
    responsedata = respondRequest(data)
    return make_response(jsonify(responsedata),200)

@app.route("/restaurant/rating/<rating>")
def rate(rating):
    return ratingfilter(respondRequest(),float(rating))
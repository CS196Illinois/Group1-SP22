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
    
def getTimeDurationOnFront(currentLoc, destLoc, mode = "walking"):
    url = "https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&"
    r = requests.get(url + "origin=" + currentLoc + "&destination=place_id:" + destLoc + "&mode=" + mode + "&key=" + API_KEY)
    time = r.json()["rows"][0]["elements"][0]["duration"]["text"]
    seconds = r.json()["rows"][0]["elements"][0]["duration"]["value"]
    return "\n Total duration will be around", time

# options to fileters are listed 
# called after the data is received and casted from request

def timefilter(reslist, currentLoc, destLoc, eatingtime, startingtime, endtime, mode = "walking"):
    filtered = []
    duration = endtime - startingtime
    for res in reslist:
        firsttime = int(getTimeDuration(currentLoc, "place_id:" + res["place_id"])) /60
        secondtime = int(getTimeDuration("place_id:" + res["place_id"],destLoc)) /60
        totaltime =  firsttime + secondtime + eatingtime
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
    sorted = reslist
    swapped = True
    while(swapped):
        swapped = False
        for i in range(len(reslist) - 1):
            if sorted[i]["name"] > sorted[i + 1]["name"]:
                sorted[i], sorted[i + 1] = sorted[i + 1], sorted[i]
                swapped = True
    return sorted

def sortByNameReverse(reslist):
    return sortByName(reslist).reverse()

def sortByPriceHigh(reslist):
    sorted = []
    copy = sortByName(reslist)
    while len(copy) != 0:
        prevPrice = 0
        index = 0
        for res in copy:
            if res["price_level"] > prevPrice:
                prevPrice = res["price_level"]
                index = copy.index(res)
        sorted.append(copy[index])
        copy.remove(index)
    return sorted

def sortByPriceLow(reslist):
    return sortByPriceHigh(reslist).reverse()

def sortByRateHigh(reslist):
    sorted = []
    copy = sortByName(reslist)
    while len(copy) != 0:
        prevRate = 0
        index = 0
        for res in copy:
            if res["rating"] > prevRate:
                prevRate = res["rating"]
                index = copy.index(res)
        sorted.append(copy[index])
        copy.remove(index)
    return sorted

def sortByRateLow(reslist):
    return sortByRateHigh(reslist).reverse()

def sortByDistanceFar(reslist, currentLoc, destLoc):
    sorted = []
    copy = sortByName(reslist)
    while len(copy) != 0:
        prevDuration = 0
        index = 0
        for res in copy:
            if getTimeDuration(currentLoc, destLoc) > prevDuration:
                prevDuration = getTimeDuration(currentLoc, destLoc)
                index = copy.index(res)
        sorted.append(copy[index])
        copy.remove(index)
    return sorted

def sortByDistanceClose(reslist, currentLoc, destLoc):
    return sortByDistanceFar(reslist, currentLoc, destLoc).reverse()

# main

def respondRequest(body):
    if "keyword" not in body.keys:
        r = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=40.110740,-88.219940&language=en&radius=" + str(body["radius"]) + "&sensor=false&key=AIzaSyBwQIJgd3BTxyNA8ccg6vcplWGA5kWNbNE&types=restaurant")
    else:
        r = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?keyword=" + body["keyword"] + "&location=40.110740,-88.219940&language=en&radius=" + str(body["radius"]) + "&sensor=false&key=AIzaSyBwQIJgd3BTxyNA8ccg6vcplWGA5kWNbNE&types=restaurant")
    res = r.text
    data = json.loads(res)
    reslist = []
    for res in data["results"]:
        reslist.append(res)
    if "rating" in body.keys:
        reslist = ratingfilter(reslist, float(body["rating"]))
    if "lowerprice" in body.keys:
        reslist = lowerpricefilter(reslist, float(body["lowerprice"]))
    if "higherprice" in body.keys:
        reslist = higherpricefilter(reslist, float(body["higherprice"]))
    if "timeinfo" in body.keys:
        reslist = timefilter(reslist, body["timeinfo"]["currentloc"], body["timeinfo"]["destloc"], body["timeinfo"]["eatingtime"], body["timeinfo"]["starttime"], body["timeinfo"]["endtime"])
    return reslist

def requesttest():
    r = requests.get("https://maps.googleapis.com/maps/api/place/nearbysearch/json?location=40.110740,-88.219940&language=en&radius=" + "100" + "&sensor=false&key=AIzaSyBwQIJgd3BTxyNA8ccg6vcplWGA5kWNbNE&types=restaurant")
    res = r.text
    data = json.loads(res)
    reslist = []
    for res in data["results"]:
        reslist.append(res)
    return reslist

@app.route("/")
def home():
    return str(timefilter(requesttest(),"1301%W%Springfield%Ave%Urbana%IL", "603%S%Wright%St%Champaign%IL", 15, 50, 90))

@app.route("/restaurant", methods=['GET'])
def rest():
    data = request.get_json()
    print(data)
    responsedata = respondRequest(data)
    return make_response(jsonify(responsedata),200)

@app.route("/restaurant/rating/<rating>")
def rate(rating):
    return ratingfilter(respondRequest(),float(rating))
from msilib.schema import AppId
from flask import Flask, render_template
import requests

api = Flask(__name__)

@api.route("/")
def home():

    r = requests.get("https://www.google.com/maps/search/?api=restaurants")
    return render_template("home.html")

@api.route("/map")
def map():
    return 1
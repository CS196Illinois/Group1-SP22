from flask import Flask, redirect, render_template, request
import requests

app = Flask(__name__)

@app.route("/temperature", methods=["POST"])
def temperature():
    zipcode = request.form["zip"]
    r = requests.get("http://api.openweathermap.org/data/2.5/weather?zip="+zipcode+",us&appid=192fba108273b0985d9f580e8ad91e0f")
    json_object = r.text
    return json_object

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
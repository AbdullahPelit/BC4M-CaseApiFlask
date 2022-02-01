import configparser
from distutils.command.config import config
from turtle import home
from urllib import request
import requests

from flask import Flask,render_template,request,url_for

app = Flask(__name__)

@app.route("/")
def homePageDashboard():
    return render_template("home.html")

@app.route("/tempurates", methods=["POST","GET"])
def showTempurates():
    city_name = request.form["cityName"]
    return "cityName: " + city_name

if __name__ == "__main__":
    app.run(debug=True)


def getApiKey():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["openweathermap"]["api"]

def getWeatherResult(city_name,api_key):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city_name,api_key)
    r = requests.get(api_url)
    return r.json()

print(getWeatherResult("London",getApiKey()))
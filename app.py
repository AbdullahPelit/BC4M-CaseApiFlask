import configparser
from distutils.command.config import config
from turtle import home
from unicodedata import name
from urllib import request
import requests

from flask import Flask, jsonify,render_template,request,url_for

app = Flask(__name__)

@app.route("/")
def getName():
    name= {
        "firstname" : "Abdullah",
        "lastname" : "PELIT"
    }
    return name

@app.route("/searchCity")
def homePageDashboard():
    return render_template("home.html")


#Post isteği gönderiyor formdan istekte bulundugumuz için.
@app.route("/tempurates", methods=["POST","GET"])
def showTempurates():
    
    city_name = request.form["cityName"]
   
    apiKey = getApiKey()
    data = getWeatherResult(city_name,apiKey)
    temp = "{0:.2f}".format(data["main"]["temp"])
    #temp = jsonify(data["main"]["temp"])
    #temp = jsonify(data["main"]["temp"])
    location = data["name"]
    #return "{tempretures: " + str(temp) + "}"
    return "Tempratures : " + temp + "    "+ "Location : " + location


#Direkt websitesi arama çubugundan şehir ismi girdiğimizde çalışıyor.
@app.route("/tempurates/<city>", methods=["GET"])
def showTempuratesTry(city):
    
    city_name = city
   
    apiKey = getApiKey()
    data = getWeatherResult(city_name,apiKey)
    temp = "{0:.2f}".format(data["main"]["temp"])
    location = data["name"]
    return "sıcaklık : " + temp
    



def getApiKey():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["openweathermap"]["api"]

def getWeatherResult(city_name,api_key):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(city_name,api_key)
    r = requests.get(api_url)

    return r.json()

def get_Name():
    name_surname = {
        "Firstname" : "Abdullah",
        "Lastname" : "PELIT"
    }
    return name_surname

if __name__ == "__main__":
    app.run(debug=True)
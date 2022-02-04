import configparser
from distutils.command.config import config
from turtle import home
from unicodedata import name
import requests

from flask import Flask, jsonify,render_template,url_for
app = Flask(__name__)

@app.route("/" , methods =["GET"])
def getName():
    
    return jsonify({"" : name})

name = {
    "firstname" : "Abdullah",
    "lastname" : "Pelit"
    }

#Direkt websitesi arama çubugundan şehir ismi girdiğimizde çalışıyor.
@app.route("/temperature/<city>", methods=["GET"])
def showTempurates(city):
    
    #showTempurates'daki parametreyle city_name eşitlendi.
    city_name = city
   
    apiKey = getApiKey()
    data = getWeatherResult(city_name,apiKey)
    temp = "{0:.2f}".format(data["main"]["temp"])
    return jsonify({"temperature" : temp})
    
#config.ini'de tuttugumuz api_keyimizi burada çekiyoruz.
def getApiKey():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config["openweathermap"]["api"]

#openweatherapi'a istek gönderiyoruz.
def getWeatherResult(city_name,api_key):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid={}".format(city_name,api_key)
    r = requests.get(api_url)
    return r.json()



#Html kullanarak arama yapmak için.
#@app.route("/searchCity")
#def homePageDashboard():
#    return render_template("home.html")


#Post isteği gönderiyor formdan istekte bulundugumuz için. /searchcity endpointiyle beraber çalışıyor.
#@app.route("/tempurates", methods=["POST","GET"])
#def showTempurates():
    
#    city_name = request.form["cityName"]
   
#    apiKey = getApiKey()
#    data = getWeatherResult(city_name,apiKey)
#    #data = request.json(getWeatherResult(city_name,apiKey))
#    temp = "{0:.2f}".format(data["main"]["temp"])
#    #temp = jsonify(data["main"]["temp"])
#    #temp = data["main"]["temp"]
#    location = data["name"]
#    #return "{tempretures: " + str(temp) + "}"
#    return "Tempratures : " + temp + "    "+ "Location : " + location

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)
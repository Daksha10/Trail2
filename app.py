from flask import Flask, render_template, request, jsonify
import requests

app=Flask(__name__)

API_KEY="beb6ae1a9367bec7eb4a8e8d9a300a91"
BASE_URL="http://api.openweathermap.org/data/2.5/weather"

@app.route("/",methods=["GET","POST"])
def index():
    if request.method=="POST":
        city=request.form.get("city")
        if not city:
            return render_template("index.html",error="City is required")
        params={
            "q" : city,
            "appid": API_KEY,
            "units":"metric"
        }
        response=requests.get(BASE_URL,params=params)
        data=response.json()
        
        if(response.status_code != 200):
            return render_template("index.html",error="Error in fetching the data")
        
        weather_data={
            "city":data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"].capitalize()
        }
        return render_template("index.html",result=weather_data)
    return render_template("index.html")

if __name__=="__main__":
    app.run()
import requests

API_KEY="868c5469fc5add3122d3e7e8313c8f3e"
Url="https://api.openweathermap.org/data/2.5/weather"

city=input("please enter the city name \n")
params={
    "q":city,
    "appid":API_KEY
}

response=requests.get(url=Url,params=params)
data=response.json()
description=data["weather"][0]["description"]
temp_inK=data["main"]["temp"]
temp=int(temp_inK)-272
print(temp)
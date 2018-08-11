import requests
city = input("Enter a City Name: ")

url ="http://api.openweathermap.org/data/2.5/weather?q={},In&APPID=6eed1261d6bafcc7bc105be4882d8a34&units=metric".format(city)
res = requests.get(url)
data = res.json()
temp = data['main']['temp']
wind_speed = data['wind']['speed']
latitude = data['coord']['lat']
longtitude = data['coord']['lon']
description = data['weather'][0]['description']

print("Temperature {} degree celcious".format(temp))
print("Wind Speed {} m/s".format(wind_speed))
print("Latitude {} ".format(latitude))
print("Longtitude {} ".format(longtitude))
print("Description {} ".format(description))



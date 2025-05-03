wx

# /bin/python
import requests

# The api key should go here

API_KEY = ""
# ..............................................

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


# To get the coordinates of the desired city
def geo_cord(city):
    try:
        sec_req = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={API_KEY}"
        sec_resp = requests.get(sec_req)
        data = sec_resp.json()
        return data[0]["lat"], data[0]["lon"]
    except:
        print("An ERROR occurred while fetching the coordinates")
        quit()    
#....................................................................


city = input("Enter a city name: ")
lat, lon = geo_cord(city)


request_url = f"{BASE_URL}?lat={lat}&lon={lon}&appid={API_KEY}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)

    print("Weather:", weather)
    print("Temperature:", temperature, "celsius")
else:
    print("An ERROR occurred")

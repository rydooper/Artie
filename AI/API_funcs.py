import requests
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def get_weather(cityName):
    apiKey = "Api key"
    baseURL = "https://api.openweathermap.org/data.2.5/weather?"
    completeURL = baseURL + "appid =" + apiKey + "&q =" + cityName
    response = requests.get(completeURL)
    x = response.JSON()  # this needs fixing~! #JSON isnt okay in response? double check that

    if x["cod"] != "404":
        y = x["main"]
        currentTemp = y["temp"]
        currentPressure = y["pressure"]
        currentHumidity = y["humidity"]
        z = x["weather"]
        weatherDescr = z[0]["description"]
        weatherStr = "The weather can be described as " + weatherDescr + ". It is " + currentTemp + " degrees with a humitidity of " + \
            currentHumidity + " and a pressure of " + \
            currentPressure + " in " + cityName + " right now."

        return weatherStr
    
def spotify_func():
    sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id="YOUR_APP_CLIENT_ID",
                                                           client_secret="YOUR_APP_CLIENT_SECRET"))
    results = sp.search(q='weezer', limit=20)
    for idx, track in enumerate(results['tracks']['items']):
        print(idx, track['name'])
    # placeholder for spotify function

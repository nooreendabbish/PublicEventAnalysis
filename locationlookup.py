import requests
import json
from geopy import geocoders
from tzwhere import tzwhere
from pytz import timezone
import pytz

def getlocation(linkIn):
    requested = requests.get(linkIn)
    userinfo = json.loads(requested.text)
    location = userinfo["location"]
    return location


username = 'nooreendabbish'
firstlink = 'https://api.github.com/users/'+username

thecity = getlocation(firstlink)
g = geocoders.GoogleV3()
place, (lat,lng) = g.geocode(thecity)
print place
print (lat, lng)
w = tzwhere.tzwhere()
print w.tzNameAt(lat, lng)

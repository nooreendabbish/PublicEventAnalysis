import requests
import json
import re
import pandas as pd
from datetime import datetime
from dateutil.parser import parse
import pickle

allEvents = []

def getpage(linkIn):
    requested =requests.get(linkIn)
    records = json.loads(requested.text)
    headerLink = requested.headers['link']
    print json.dumps(records, sort_keys=True, indent=4, separators=(',',':'))
    events = [(records[x]["created_at"],
               records[x]["type"]) for x in range(0,len(records))]
    allEvents.extend(events)

    p = re.compile('\<.*\>; rel="next"')
    
    if None != p.match(headerLink):
        getpage(p.findall(headerLink)[0][:-13][1:])
        
username = 'mbostock'
firstlink = 'https://api.github.com/users/'+username+'/events/public'

getpage(firstlink)
now = datetime.now()
print now

f = open("mbostockPublicEvents.txt", "w")
pickle.dump(allEvents, f)

import pickle
import datetime
from dateutil.parser import parse
import matplotlib.pyplot as plt
import numpy as np

f = open("mbostockPublicEvents.txt", "r")
events = pickle.load(f)
f.close()

eventList = [list(x) for x in events]
for i in range(0,len(eventList)):
    eventList[i].extend([parse(eventList[i][0]).weekday()])

days = range(0,6)
weekdayEvents = [[int(x[0][11:13]), x[1]] for x in eventList if x[2] in days]

days = range(6,8)
weekendEvents = [[int(x[0][11:13]), x[1]] for x in eventList if x[2] in days]

def eventTally(events): 
    tally = [0]*24
    for i in range(0,len(events)):
        for j in range(0,24):
            if events[i][0] == j:
                tally[j] += 1
    return tally

weekendTally = eventTally(weekendEvents)
weekdayTally = eventTally(weekdayEvents)






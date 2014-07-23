import pickle
import datetime
from dateutil.parser import parse
import matplotlib.pyplot as plt
import numpy as np

f = open("mbostockPublicEvents.txt", "r")
events = pickle.load(f)
f.close()

#in events item 0 = timestampe
#          item 1 = type


boutDefn = 10
boutTime = datetime.timedelta(hours=3)
bouts = []
boutCount = 0
for i in range(len(events)):
    itemTimeStamp = (parse(events[i][0]))
    if (i+boutDefn) < len(events):
        if (itemTimeStamp - parse(events[i+boutDefn][0]) < boutTime):
            if i not in bouts:
                boutCount += 1
            for j in range(i, i+boutDefn):
                if j not in bouts:
                     bouts.extend([j])
types = {'PushEvent':'push',
         'CreateEvent':'create',
         'IssueCommentEvent':'comment',
         'PullRequestEvent':'pull',
         'DeleteEvent':'delete',
         'ReleaseEvent':'release',
         'IssuesEvent':'issue',
         'GollumEvent':'gollum',
         'PullRequestReviewCommentEvent':'review'}
seqout =""
boutstring = ""
for i in range(len(bouts)):
    eventType = types[events[bouts[i]][1]]
    boutstring += eventType+'-'
    if i == (len(bouts)-1):
        seqout +=boutstring+'end'
        boutstring = ""
    elif (not bouts[i+1] == bouts[i]+1):
        seqout +=boutstring+'end\n'
        boutstring = ""
print seqout
f = open("../d3 Notepad/fourth.csv", "w")
f.write(seqout)
f.close

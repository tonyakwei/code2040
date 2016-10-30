import json
import requests
import datetime
import calendar
from pytz import timezone


HTTPHeaders = {'content-type': 'application/json'}
tokenDict = {'token': '5185bcac830273a1051d4c260585f734'}
challengeURL = 'http://challenge.code2040.org/api/dating'
validationURL = 'http://challenge.code2040.org/api/dating/validate'

dateDict = json.loads(requests.post(challengeURL, data=json.dumps(tokenDict), headers=HTTPHeaders).text)
datestamp = dateDict['datestamp']
interval = dateDict['interval']

# print datestamp
# print interval

year = datestamp[0:4]
month = datestamp[5:7]
day = datestamp[8:10]
hour = datestamp[11:13]
minute = datestamp[14:16]
second = datestamp[17:19]



date = datetime.datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))
epochTime = calendar.timegm(date.timetuple())
epochTime += int(interval)
epochTime += 18000 #Timezone EST to UTC shift
print epochTime
dateIntermediate = datetime.datetime.fromtimestamp(epochTime)
date2 = timezone('US/Eastern').localize(dateIntermediate)

year2 = date2.year
month2 = date2.month
day2 = date2.day
hour2 = date2.hour
minute2 = date2.minute
second2 = date2.second

if date2.year < 10:
    year2 = "0" + str(year2)

if date2.month < 10:
    month2 = "0" + str(month2)

if date2.day < 10:
    day2 = "0" + str(day2)

if date2.hour < 10:
    hour2 = "0" + str(hour2)

if date2.minute < 10:
    minute2 = "0" + str(minute2)

if date2.second < 10:
    second2 = "0" + str(second2)


answerDate = str(year2) + "-" + str(month2) + '-' + str(day2) + 'T' + str(hour2) + ":" + str(minute2) + ":" + str(second2) + "Z"
answerDate = unicode(answerDate)

answerResponse = {'token': '5185bcac830273a1051d4c260585f734', 'datestamp': answerDate}

print answerResponse['datestamp']

response = requests.post(validationURL, data=json.dumps(answerResponse), headers=HTTPHeaders)

print response.text

#Interestingly, datetime seemed to contain information about the timezone. I added five hours to shift the date to UTC
#before sending it to the server. This likely would cause trouble with computers in other timezones.

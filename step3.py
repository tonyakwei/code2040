import json
import requests

HTTPHeaders = {'content-type': 'application/json'}
tokenDict = {'token': '5185bcac830273a1051d4c260585f734'}
challengeURL = 'http://challenge.code2040.org/api/haystack'
validationURL = 'http://challenge.code2040.org/api/haystack/validate'

needleHaystackDict = json.loads(requests.post(challengeURL, data=json.dumps(tokenDict), headers=HTTPHeaders).text)

needle = needleHaystackDict['needle']
index = 0;

for i in range(0, len(needleHaystackDict['haystack'])-1):
    if needle == needleHaystackDict['haystack'][i]:
        index = i
        break

answerDict = {'token': '5185bcac830273a1051d4c260585f734', 'needle': index}

response = requests.post(validationURL, data=json.dumps(answerDict), headers=HTTPHeaders)

print response.text

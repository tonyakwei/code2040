import json
import requests


HTTPHeaders = {'content-type': 'application/json'}
tokenDict = {'token': '5185bcac830273a1051d4c260585f734'}
challengeURL = 'http://challenge.code2040.org/api/prefix'
validationURL = 'http://challenge.code2040.org/api/prefix/validate'

prefixDict = json.loads(requests.post(challengeURL, data=json.dumps(tokenDict), headers=HTTPHeaders).text)
prefix = prefixDict['prefix']
prefixLength = len(prefix)

words = []

for i in range(0, len(prefixDict['array'])-1):
    if(prefixDict['array'][i][0:prefixLength] != prefix):
        words.append(unicode(prefixDict['array'][i]))

# print prefixDict['prefix']
# print prefixDict['array']
# print words

answerDict = {'token': '5185bcac830273a1051d4c260585f734', 'array': words}
# print answerDict

response = requests.post(validationURL, data=json.dumps(answerDict), headers=HTTPHeaders)

print response.text

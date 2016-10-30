import json
import requests

HTTPHeaders = {'content-type': 'application/json'}
tokenDict = {'token': '5185bcac830273a1051d4c260585f734'}
challengeURL = 'http://challenge.code2040.org/api/reverse'
validationURL = 'http://challenge.code2040.org/api/reverse/validate'



response1 = requests.post(challengeURL, data=json.dumps(tokenDict), headers=HTTPHeaders)
reverseString = response1.text[::-1]

answerDict = tokenDict = {'token': '5185bcac830273a1051d4c260585f734', 'string': reverseString}

response2 = requests.post(validationURL, data=json.dumps(answerDict), headers=HTTPHeaders)

print response2.text

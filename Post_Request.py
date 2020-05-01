import requests
import json

def postRequest(APIEndpoint,JSONData):
    response = requests.post(url=APIEndpoint, json=JSONData)

    responseText = response.json()

    return responseText

# Attributes
APIEndpoint = 'http://127.0.0.1:5000/new'
data = {'intent_name':'service_issue','keywords':['activ', 'deactiv', 'packag']}
json_data = json.dumps(data)

res = postRequest(APIEndpoint,json_data)


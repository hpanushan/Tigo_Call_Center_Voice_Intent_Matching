import requests
import json

def postRequest(APIEndpoint,JSONData):
    response = requests.post(url=APIEndpoint, json=JSONData)

    responseText = response.json()

    return responseText

# Attributes
#APIEndpoint = 'http://35.232.85.245:5000/preparation'
#data = {'checked_t': ["Recording (2).wav",] ,'checked_v': ["Network_Failure_01.wav"], 'move_to_voice_clips': 'true'}


APIEndpoint = 'http://35.232.85.245:5000/execute'
data = {'file_name': "Recording (2).wav"}
json_data = json.dumps(data)

res = postRequest(APIEndpoint,json_data)

print(res)

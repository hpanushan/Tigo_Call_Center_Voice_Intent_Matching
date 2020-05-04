import requests
import json

def postRequest(APIEndpoint,JSONData):
    response = requests.post(url=APIEndpoint, json=JSONData)

    responseText = response.json()

    return responseText

# Attributes
#APIEndpoint = 'http://35.232.85.245:5000/preparation'
#data = {'checked_t': ["Network_Failure_01.wav",] ,'checked_v': ["Network_Failure_01.wav"], 'move_to_voice_clips': 'true'}


#PIEndpoint = 'http://35.232.85.245:5000/execute'
#data = {'file_name': "Network_Failure_01.wav"}
#json_data = json.dumps(data)

#res = postRequest(APIEndpoint,json_data)

#print(res)

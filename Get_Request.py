import requests

def getRequest(APIEndpoint):
    # This can output get request JSON
    response = requests.get(url=APIEndpoint)

    # Extracting the data in JSON format
    data = response.json()

    return data

print(getRequest('http://127.0.0.1:5000/intent'))
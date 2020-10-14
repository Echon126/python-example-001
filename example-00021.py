import requests
import json

data = {"info": "zczxcz"}
url = "http://127.0.0.1:9090/test/python"
headers = {'Accept': '*/*', 'Cache-Control': 'no-cache'}
response = requests.post(url, data=data, headers=headers)
print(response.text)

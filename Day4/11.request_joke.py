import requests
import json

headers = {
    "Accept":"application/json"
}
response =requests.get("https://icanhazdadjoke.com/", headers=headers)
print(response)
print(response.status_code)
print(response.content)
json_dict = json.loads(response.content)
print(json_dict)

print(json_dict['joke'])
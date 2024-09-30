import requests

response =requests.get("https://www.michelin.ro/")
print(response)
print(response.status_code)
print(type(response.content))
print(response.text)
print(type(response.text))


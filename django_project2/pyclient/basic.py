import requests

endpoint='https://httpbin.org/json'
get_request=requests.get(endpoint)
print(get_request.json())

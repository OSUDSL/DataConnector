import json
import requests

data = { "velocity" : 503 }
print("Test correct post")
r = requests.post('http://127.0.0.1:5000/update', json=data)
print(r)
# test incorrect client requests
# 1. send the dictionary as a string instead of json
print("Test bad post data")
r = requests.post('http://localhost:5000/update', data=data)
print(r)

# 2. request unknown url
print("Test wrong url path")
r = requests.post('http://localhost:5000/wrong', json=data)
print(r)

# 3. pass data to get target
print("Test extra data in get call")
r = requests.get('http://localhost:5000/', params="junk")
print(r)

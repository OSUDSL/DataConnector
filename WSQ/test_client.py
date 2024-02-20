import sys
import json
import requests

person = {"name": "<NAME>",
           "gender": "male",
           "birthDate": "Feb 30th"}
# dumps converts python objects into a json string
s = json.dumps(person)
r = requests.post('http://localhost:5000/', json=s)

r = requests.get('http://localhost:5000/')
print(r.text)

r = requests.delete('http://localhost:5000/', params={'name': 'Tiya'})
print(r.text)
r = requests.get('http://localhost:5000/')
print(r.text)
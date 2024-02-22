import json
import requests

data = {"Velocity": 500}
r = requests.post('http://localhost:5000/update', json=data)

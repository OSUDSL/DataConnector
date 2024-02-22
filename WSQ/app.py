from flask import Flask, jsonify, request
import json

# create new flask application
app = Flask(__name__)
app.config["DEBUG"] = True

# test data in the form of a dict (map)
people = [
    { 'name': 'Tiya',
      'gender': 'female',
      'birthdate': 'June 1st'},
    { 'name': 'Anya',
      'gender': 'female',
      'birthdate': 'idk' }
]
@app.route('/', methods=['GET'])
def get_people():
    return jsonify(people)

def get_person(name):
    for person in people:
        if person['name'] == name:
            return person
    return None

@app.route('/', methods=['POST'])
def create_people():
    data = request.get_json()
    person = json.loads(data)
    people.append(person)
    return ""

@app.route('/', methods=["DELETE"])
def delete_people():
    # add try-except statements in case the json isn't formatted properly
    data = request.get_json()
    name = json.loads(data)
    name = name['name']
    for p in people:
        if p['name'] == name:
            people.remove(p)
            break
    return ""

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()

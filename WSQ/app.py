from flask import Flask, jsonify, request
import json

# create new flask application
app = Flask(__name__)
app.config["DEBUG"] = True

# test data in the form of a dict (map)
people = [
    { 'id': 1,
      'name': 'Tiya',
      'gender': 'female',
      'birthdate': 'June 1st'},
    { 'id': 2,
      'name': 'Anya',
      'gender': 'female',
      'birthdate': 'idk' }
]
next_person_id = 3
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
    global next_person_id
    data = request.get_json()
    person = json.loads(data)
    person['id'] = next_person_id
    next_person_id += 1
    people.append(person)
    return ""

# issue in delete_people: for some reason, it keeps saying that no value for name was passed
@app.route('/', methods=["DELETE"])
def delete_people(name):
    global next_person_id
    person = get_person(name)
    for p in people:
        if p['name'] == name:
            people.remove(p)
            break
    return person

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()

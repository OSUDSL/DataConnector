from flask import Flask, jsonify, request
import json
from werkzeug.exceptions import BadRequest

# create new flask application
app = Flask(__name__)
app.config["DEBUG"] = True

info = {
        "Velocity": 23.46,
        "SimTime": 0.3223,
        "XPos": 234.5432,
    }

@app.route('/', methods=["GET"])
def get_dict():
    return jsonify(info)

@app.route('/update', methods=["POST"])
def update_dict():
    try:
        data = request.get_json()
        info.update(data)
    except json.JSONDecodeError as e:
        return "Error"
    except TypeError:
        return "Error"
    return ""

# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()

import json
import subprocess
from flask import Flask, request
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app, resources={r"/": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'
app.config.from_pyfile('config.py')
apiKey = app.config['API_KEY']


@app.route('/', methods=["GET", "OPTIONS"])
@cross_origin(origin='*', headers=['Content-Type'])
def home():
    return {'author': 'Tech Team', 'description': 'ProjectX Website Information API'}


@app.route('/<collection>/<collectionId>', methods=["GET", "OPTIONS"])
@cross_origin(origin='*', headers=['Content-Type'])
def get_data(collection, collectionId):
    output = subprocess.run(
        f"./fetch_command.sh {collection} {apiKey}", shell=True, capture_output=True)
    data = json.loads(output.stdout.decode())

    if not data:
        return []

    if collectionId != 'all':
        for item in data:
            if item["id"] == collectionId:
                return item

    return data


if __name__ == "__main__":
    app.run(host='127.0.0.1')

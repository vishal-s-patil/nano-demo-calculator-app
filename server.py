from flask import Flask, request, jsonify
import json

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world!'

@app.route("/calculator/add", methods=['POST'])
def add():
    if request.method == 'POST':
        f = json.loads(request.get_data().decode('utf8'))
        data = {
            "result": f["first"]+f["second"]
        }
        return jsonify(data)

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    if request.method == 'POST':
        f = json.loads(request.get_data().decode('utf8'))
        data = {
           "result": f["first"]-f["second"]
        }
        return jsonify(data)

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')

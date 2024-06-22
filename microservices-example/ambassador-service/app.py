import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process', methods=['POST'])
def process():
    data = request.json
    service = data.get('service')

    if service == 'python':
        response = requests.post('http://python-service:5000/process', json=data)
    elif service == 'node':
        response = requests.post('http://node-service:3000/process', json=data)
    else:
        return jsonify({"error": "Unknown service"}), 400

    return jsonify(response.json())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

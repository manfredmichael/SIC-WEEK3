from flask import Flask, request, Response
import json

app = Flask(__name__)


temp_list = []


@app.route('/sensor/data', methods=["POST", "GET"])
def sensor():
    if request.method == 'POST':
        data = request.get_json()
        temperature = data["temperature"]
        kelembapan = data["kelembapan"]
        timestamp = data["timestamp"]

        temp_list.append([temperature, kelembapan, timestamp])

        data = {
            'message': 'Data saved successfully'
        }
    else: 
        data = {
            'temperature_list': temp_list
        }

    response = Response(
        json.dumps(data),
        status=200,
        mimetype='application/json'
    )

    return response

if __name__ == '__main__':
    app.run(debug=True)
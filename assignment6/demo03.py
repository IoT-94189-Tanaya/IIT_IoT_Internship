from flask import Flask, request, jsonify

app = Flask(__name__)

TEMP_FILE = "temperature.txt"
LIGHT_FILE = "light.txt"

@app.route('/send_data', methods=['POST'])
def receive_data():
    data = request.json

    temperature = data.get("temperature")
    light = data.get("light")

    if temperature is None or light is None:
        return jsonify({"error": "Missing data"}), 400

   
    with open(TEMP_FILE, "a") as t:
        t.write(str(temperature) + "\n")

 
    with open(LIGHT_FILE, "a") as l:
        l.write(str(light) + "\n")

    return jsonify({"message": "Data stored successfully"}), 200


@app.route('/get_temperature', methods=['GET'])
def get_temperature():
    try:
        with open(TEMP_FILE, "r") as t:
            data = t.read()
        return f"<h2>Temperature Readings</h2><pre>{data}</pre>"
    except FileNotFoundError:
        return "No temperature data available"


@app.route('/get_light', methods=['GET'])
def get_light():
    try:
        with open(LIGHT_FILE, "r") as l:
            data = l.read()
        return f"<h2>Light Intensity Readings</h2><pre>{data}</pre>"
    except FileNotFoundError:
        return "No light data available"


if __name__ == "__main__":
    app.run(debug=True)
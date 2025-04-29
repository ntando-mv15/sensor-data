from flask import Flask, jsonify
from app.helpers import fetch_temperature_from_box

app = Flask(__name__)

APP_VERSION = "v0.1.0"

BOX_IDS = [
    "5eba5fbad46fb8001b799786",
    "5c21ff8f919bf8001adf2488",
    "5ade1acf223bd80019a1011c"
]

@app.route("/temperature")
def get_average_temperature():
    temperatures = []
    for box_id in BOX_IDS:
        temp = fetch_temperature_from_box(box_id)
        if temp is not None:
            temperatures.append(temp)

    if temperatures:
        avg_temp = sum(temperatures) / len(temperatures)
        return jsonify({"average_temperature": round(avg_temp, 2)})
    else:
        return jsonify({"error": "No recent temperature data found."}), 404

@app.route("/version")
def version():
    return jsonify({"App version": APP_VERSION})

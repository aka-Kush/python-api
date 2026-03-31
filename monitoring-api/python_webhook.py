import random

import requests
from flask import Flask, json, jsonify

WEBHOOK_URL = "http://localhost:5001/alarm"
THRESHOLD = 80

app = Flask(__name__)


@app.route("/simulate", methods=["GET"])
def simulate_alarm():
    value = random.randint(50, 100)
    print(f"Generate value = {value}")

    try:
        if value >= THRESHOLD:
            requests.post(WEBHOOK_URL, json={"value": value, "threshold": THRESHOLD})
    except Exception as e:
        print(f"Error with webhook: {e}")

    return jsonify({"value": value, "threshold": THRESHOLD})


if __name__ == "__main__":
    app.run(port=5000)

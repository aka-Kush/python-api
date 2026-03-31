import threading

from flask import Flask, request

app = Flask(__name__)


def beep():
    print("BEEEEPINGGGGG!!!!!!!!")


@app.route("/alarm", methods=["POST"])
def alarm():
    data = request.json
    print(f"Threshold value reached!")
    threading.Thread(target=beep).start()
    return "", 200


if __name__ == "__main__":
    app.run(port=5001)

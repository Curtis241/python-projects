from flask import Flask, jsonify
app = Flask(__name__)


@app.route("/")
def mdu_gateway():
    return jsonify({"gateway": {"name": "MDU Gateway 1"}})

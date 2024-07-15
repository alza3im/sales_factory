from flask import Flask, jsonify, request
from flask_cors import CORS
from utils import hash_base62

app = Flask(__name__)
CORS(app)


data = {
        "items": [
            {"google.com": ""},
            {"openai.com": ""},
        ]
}

@app.route("/")
def hello_world():
    return jsonify({"message": "Hello, World!"})


@app.route("/api/data/<string:url>",methods=['POST'])
def generate_short_link(url):
    new_url = hash_base62(url)
    data["items"].append({url: new_url})
    return jsonify({"message": "Success!", "code": 200, "short_url": new_url})

@app.route("/api/data")
def get_data():
    return jsonify({"data": data, "message": "Success!", "code": 200 })


if __name__ == "__main__":
    app.run(debug=True)
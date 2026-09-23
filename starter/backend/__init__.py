import os
from flask import Flask, jsonify
from flask_cors import CORS

from .movies import movies_api

app = Flask(__name__)
CORS(app)
app.register_blueprint(movies_api)


@app.route("/", methods=["GET"])
def index():
    return jsonify({
        "message": "Movie Picture API",
        "routes": [
            "/",
            "/movies",
            "/movies/<id>",
        ],
    })


# Start app
if __name__ == "__main__":
    app.run(
        debug=True,
        host="0.0.0.0",
        port=int(os.getenv("FLASK_RUN_PORT", 5000)),
    )

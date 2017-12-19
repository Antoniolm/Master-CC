from flask import Flask
from flask import jsonify
app = Flask(__name__)

@app.route("/")
def getRoot():
    return jsonify(
        status="OK",
    )

@app.route("/status")
def getStatus():
    return jsonify(
        status="OK",
    )


if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

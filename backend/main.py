import flask

app = flask.Flask(__name__)

@app.route("/")
def index():
    return "Hello, you are on backend flask server"

@app.route('/api/test/')
def test():
    testDict = {
        'keyA': "string",
        'keyB': [1,4,6,3,4],
        'keyC': 34,
    }

    return flask.jsonify(testDict)

if __name__ == "__main__":
    app.run(debug=True)
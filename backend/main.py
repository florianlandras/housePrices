import flask
from postProcess.getdata import getdef
from postProcess.geturl import newUrl
import pandas

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

@app.route('/api/getData/')
def data():

    baseUrl = 'https://www.hemnet.se/salda/'
    city = 'soderkopings-kommun'
    urlStr = newUrl(baseUrl+city)
    df = getdef(urlStr)
    return flask.jsonify(df.to_dict(orient='index'))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
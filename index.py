from os import system
from subprocess import getoutput
from flask import Flask, request
from urllib.parse import urlencode
import requests


app = Flask(__name__)
@app.route("/")
def index():
    args = request.args
    return requests.get("http://127.0.0.1:1234/sub?"+urlencode(args)).text, {'Content-Type': 'text/yaml;charset=utf-8'}

if __name__ == "__main__":
    system("sh start.sh")
    # app.run(host="0.0.0.0", port=221, debug=False)
    server = pywsgi.WSGIServer(('0.0.0.0', 221), app)
    server.serve_forever()

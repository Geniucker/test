from os import system
from subprocess import getoutput
from flask import Flask, request
from urllib.parse import urlencode
import requests
from ping3 import ping


app = Flask(__name__)
@app.route("/")
def index():
    args = request.args
    # return requests.get("http://127.0.0.1:1234/sub?"+urlencode(args)).text, {'Content-Type': 'text/yaml;charset=utf-8'}
    return str(ping('localhost'))

if __name__ == "__main__":
    system("subconverter/subconverter &")
    app.run(host="0.0.0.0", port=221, debug=True)

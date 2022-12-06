from os import system
from subprocess import getoutput
from flask import Flask


# app = Flask(__name__)
# @app.route("/")
# def index():
system("nohup subconverter/subconverter")
#    return getoutput("subconverter/subconverter")


#if __name__ == "__main__":
#    app.run(host="0.0.0.0", port=221, debug=True)

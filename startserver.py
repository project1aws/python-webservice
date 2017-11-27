from flask import Flask, request
from flask_restful import Resource, Api
#from sqlalchemy import create_engine
#from json import dumps
#from flask.ext.jsonpify import jsonify
#import random

app = Flask(__name__)
@app.route('/')
def index():
     return "OK Test"
if __name__=='__main__':
    app.run(host="0.0.0.0", port=5000)

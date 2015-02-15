from flask import Flask, jsonify, request, render_template, redirect, Response
from flask.ext.mongoengine import MongoEngine

import os

app = Flask(__name__)

def getenv(key):
    val = os.environ.get(key)
    if val:
        return val
    elif os.path.isfile('.env'):
        f = open('.env')
        s = f.read()
        f.close()
        for line in s.strip().split('\n'):
            k, v = line.split('=')
            if k == key:
                return v
    return None

app.config['MONGODB_SETTINGS'] = {
    'db': 'infection',
    'host': getenv('MONGOLAB_URI'),
}
db = MongoEngine(app)
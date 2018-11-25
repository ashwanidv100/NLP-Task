import os
import logging
import redis
import gevent
from flask import Flask, render_template
from flask_sockets import Sockets

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('base.html')

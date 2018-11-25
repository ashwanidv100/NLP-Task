"""
@author: ashwanidv100

"""

from flask import Flask

app = Flask(__name__)
app.config.from_object('config') # configuration file


from app import views

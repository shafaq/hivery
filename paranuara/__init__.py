from flask import Flask
from flask_pymongo import PyMongo


app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'test_db'

mongo = PyMongo(app)

from . import api

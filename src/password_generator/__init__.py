from flask import Flask
from flask_mongoengine import MongoEngine


app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    "db": "db_password_generator",
}

db = MongoEngine(app)

from . import urls

from flask import Flask
from flask_apscheduler import APScheduler
from flask_mongoengine import MongoEngine

from .config import Config


app = Flask(__name__)
app.config.from_object(Config())

db = MongoEngine(app)

scheduler = APScheduler()
scheduler.init_app(app)
scheduler.start()

from . import tasks
from . import urls

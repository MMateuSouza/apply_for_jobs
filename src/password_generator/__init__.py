from flask import Flask
from flask_apscheduler import APScheduler
from flask_mongoengine import MongoEngine


# TODO: Utilizar o arquivo `config.py` para parametrizar variáveis de ambiente...
app = Flask(__name__)
app.config["MONGODB_SETTINGS"] = {
    "db": "local",
    "host": "127.0.0.1",
    "port": 27017,
}

db = MongoEngine(app)

scheduler = APScheduler()
scheduler.api_enabled = True
scheduler.timezone = "America/Manaus"
scheduler.init_app(app)
scheduler.start()

from . import tasks
from . import urls

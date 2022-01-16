from flask import Flask, render_template, request

from .helpers import json_serial
from .forms import PasswordForm

import json
import requests

app = Flask(__name__)


@app.route("/", methods=["GET", ])
def index():
    return render_template("index.html")


@app.route("/new_password/", methods=["GET", "POST"])
def new_password():
    form = None

    if request.method == "GET":
        form = PasswordForm()

    elif request.method == "POST":
        form = PasswordForm(request.form)

        if form.validate():
            form.data.pop("allow_letters", None)
            headers = {"Content-Type": "application/json"}
            r = requests.post("http://localhost:5000/passwords/", data=json.dumps(form.data, default=json_serial), headers=headers)
            print(r.json())
    return render_template("new_password.html", form=form)

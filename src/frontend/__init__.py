from flask import flash, Flask, redirect, render_template, request, url_for

from .config import Config
from .helpers import json_serial
from .forms import PasswordForm

import json
import requests

app = Flask(__name__)
app.config.from_object(Config())


@app.route("/", methods=["GET", ])
def index():
    r = requests.get(app.config["PASSWORDS_API"])
    data = r.json()
    passwords = data["passwords"] if "passwords" in data else []
    return render_template("index.html", passwords=passwords)


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
            r = requests.post(app.config["PASSWORDS_API"], data=json.dumps(form.data, default=json_serial), headers=headers)

            if r.status_code == 200:
                flash("Senha cadastrada com sucesso!")
                return redirect(url_for("index"))

    return render_template("new_password.html", form=form)

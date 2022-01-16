from flask import Flask, render_template, request

import json
import requests

app = Flask(__name__)


@app.route("/", defaults={"path": "index"})
@app.route("/<path:path>/", methods=["GET", "POST"])
def catch_all(path):
    try:
        if path == "new_password" and request.method == "POST":
            form = request.form

            headers = {"Content-Type": "application/json"}
            data = {
                "description": form.get("description", None),
                "expires_at": form.get("expires_at", None),
                "max_value_for_viewing": form.get("max_value_for_viewing", None),
                "length": int(form.get("length", None)),
                "allow_numbers": form.get("allow_numbers", None) == "on",
                "allow_special_characters": form.get("allow_special_characters", None) == "on",
                "allow_uppercase_letters": form.get("allow_uppercase_letters", None) == "on",
                "allow_lowercase_letters": form.get("allow_lowercase_letters", None)  == "on",
            }
            r = requests.post("http://localhost:5000/passwords/", data=json.dumps(data), headers=headers)

        return render_template(f"{path}.html")
    except:
        return "Page not found", 404

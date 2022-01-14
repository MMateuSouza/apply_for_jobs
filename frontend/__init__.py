from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", defaults={"path": "index"})
@app.route("/<path:path>/")
def catch_all(path):
    try:
        return render_template(f"{path}.html")
    except:
        return "Page not found", 404

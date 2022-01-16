from crypt import methods
from . import app, views

password_view = views.PasswordAPI.as_view("password_api")

app.add_url_rule("/passwords/", view_func=password_view, methods=["GET", "POST"])
app.add_url_rule("/passwords/<uuid:id>/", view_func=password_view, methods=["GET", "PUT", "DELETE"])

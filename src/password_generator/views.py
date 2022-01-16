import imp
from flask.views import MethodView

from .models import Password


class PasswordAPI(MethodView):
    def get(self, id=None):
        if id:
            return f"[GET] Password API - id = {id}"

        return f"[GET] Password API"

    def post(self):
        return "[POST] Password API"

    def put(self, id):
        return "[PUT] Password API"

    def delete(self, id):
        return "[DELETE] Password API"

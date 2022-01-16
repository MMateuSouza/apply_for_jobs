import imp
from flask.views import MethodView


class PasswordAPI(MethodView):
    def get(self, pk=None):
        if pk:
            return f"[GET] Password API - pk = {pk}"

        return f"[GET] Password API"

    def post(self):
        return "[POST] Password API"

    def put(self, pk):
        return "[PUT] Password API"

    def delete(self, pk):
        return "[DELETE] Password API"

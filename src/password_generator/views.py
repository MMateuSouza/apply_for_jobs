from flask import  request, Response
from flask.views import MethodView

from .models import Password


class PasswordAPI(MethodView):
    def get(self, id=None):
        if id:
            try:
                password = Password.objects.with_id(id)
                password.visualize()
                return password.to_json(), 200
            except:
                return {}, 404

        passwords = Password.objects.all().exclude("password")
        return Response([password.to_json() for password in passwords])

    def post(self):
        try:
            data = request.get_json()

            kwargs = {
                "length": data.get("length", 10),
                "allow_numbers": data.get("allow_numbers", True),
                "allow_special_characters": data.get("allow_special_characters", True),
                "allow_uppercase_letters": data.get("allow_uppercase_letters", True),
                "allow_lowercase_letters": data.get("allow_lowercase_letter", True),
            }

            # Remover os atributos não pertencentes ao documento Password
            # Evitar excessão -> mongoengine.errors.FieldDoesNotExist: The fields "{kwargs**}" do not exist on the document "Password"
            for kwarg in kwargs:
                data.pop(kwarg, None)

            password = Password(**data)
            password.set_password(**kwargs)
            password.save()
            # Retornar todos os campos com excessão do campo senha
            password.password = None
            return password.to_json(), 200
        except Exception as e:
            return {"message": str(e)}, 404

    def put(self, id):
        return "[PUT] Password API"

    def delete(self, id):
        return "[DELETE] Password API"

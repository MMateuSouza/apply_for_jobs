from flask import  jsonify, request
from flask.views import MethodView

from .helpers import password_serializer, passwords_serializer
from .models import Password


class PasswordAPI(MethodView):
    def get(self, id=None):
        if id:
            try:
                password = Password.objects.with_id(id)
                password.visualize()
                return password_serializer(password), 200
            except:
                return {}, 404

        data = Password.objects.all().exclude("password")
        passwords = passwords_serializer(data)

        return jsonify({"passwords": passwords})

    def post(self):
        try:
            data = request.get_json()

            kwargs = {
                "length": data.get("length", 10),
                "allow_numbers": data.get("allow_numbers", True),
                "allow_letters": data.get("allow_letters", True),
                "allow_special_characters": data.get("allow_special_characters", True),
                "allow_uppercase_letters": data.get("allow_uppercase_letters", True),
                "allow_lowercase_letters": data.get("allow_lowercase_letters", True),
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
            return password_serializer(password), 200
        except Exception as e:
            return {"message": str(e)}, 404

    def put(self, id):
        return "[PUT] Password API"

    def delete(self, id):
        return "[DELETE] Password API"

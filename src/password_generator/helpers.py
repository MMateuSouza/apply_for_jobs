from flask import request, url_for

import string
import secrets


def password_serializer(password):
    return {
        "id": password["id"],
        "description": password["description"],
        "password": password["password"] if "password" in password else None,
        "performed_views": password["performed_views"],
        "max_value_for_viewing": password["max_value_for_viewing"],
        "created_at": password["created_at"].strftime("%d/%m/%Y %H:%M"),
        "expires_at": password["expires_at"].strftime("%d/%m/%Y %H:%M"),
        "link": f"{request.url_root}{url_for('password_api', id=password['id'])}",
    }


def passwords_serializer(passwords):
    passwords_lst = []

    for _ in passwords:
        passwords_lst.append(password_serializer(_))

    return passwords_lst


def handler(event):
    """Signal decorator to allow use of callback functions as class decorators."""
    # http://docs.mongoengine.org/guide/signals.html#attaching-events
    def decorator(fn):
        def apply(cls):
            event.connect(fn, sender=cls)
            return cls

        fn.apply = apply
        return fn

    return decorator


class PasswordGenerator():

    @staticmethod
    def generate(length, allow_numbers, allow_special_characters, allow_uppercase_letters, allow_lowercase_letters, **kwargs) -> str:
        condition = ""

        if allow_numbers:
            condition += string.digits

        if allow_special_characters:
            condition += string.punctuation

        if allow_uppercase_letters:
            condition += string.ascii_uppercase

        if allow_lowercase_letters:
            condition += string.ascii_lowercase

        return "".join((secrets.choice(condition)) for i in range(length))


if __name__ == "__main__":
    def main() -> None:
        try:
            password_length = int(input("Comprimento das senhas: "))

            print(f"Senha numérica: {PasswordGenerator.generate(password_length, True, False, False, False)}")
            print(f"Senha com apenas caracteres especiais: {PasswordGenerator.generate(password_length, False, True, False, False)}")
            print(f"Senha com letras maiúsculas: {PasswordGenerator.generate(password_length, False, False, True, False)}")
            print(f"Senha com letras minúsculas: {PasswordGenerator.generate(password_length, False, False, False, True)}")
            print(f"Senha com todas as opções: {PasswordGenerator.generate(password_length, True, True, True, True)}")

        except ValueError:
            print("É necessário um valor numérico para o comprimento, favor tentar novamente...")
            main()

    main()

import string
import secrets


class PasswordGenerator():

    @staticmethod
    def generate(length, allow_numbers, allow_special_characters, allow_uppercase_letters, allow_lowercase_letters,) -> str:
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

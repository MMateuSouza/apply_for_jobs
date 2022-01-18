from dotenv import load_dotenv

import os


load_dotenv()


class Config(object):
    ENV = os.getenv("ENV", "development")
    DEBUG = os.getenv("DEBUG", True)
    SECRET_KEY = os.getenv("SECRET_KEY", "SECRET_KEY")

    PASSWORDS_API = os.getenv("PASSWORDS_API", "http://localhost:5000/passwords/")

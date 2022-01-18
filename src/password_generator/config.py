from dotenv import load_dotenv

import os


load_dotenv()


class Config(object):
    ENV = os.getenv("ENV", "development")
    DEBUG = os.getenv("DEBUG", True)
    SECRET_KEY = os.getenv("SECRET_KEY", "SECRET_KEY")

    MONGODB_DB = os.getenv("MONGODB_DB", "local")
    MONGODB_HOST = os.getenv("MONGODB_HOST", "127.0.0.1")
    MONGODB_PORT = os.getenv("MONGODB_PORT", 27017)
    MONGODB_USERNAME = os.getenv("MONGODB_USERNAME", None)
    MONGODB_PASSWORD = os.getenv("MONGODB_PASSWORD", None)
    # Caso não queira que a conexão com o banco seja realizada
    # no momento da instanciação, deixar `MONGODB_CONNECT = False`,
    # a conexão será criada apenas na primeira tentativa de acesso.
    MONGODB_CONNECT = os.getenv("MONGODB_CONNECT", False)

    SCHEDULER_API_ENABLED = os.getenv("SCHEDULER_API_ENABLED", False)
    SCHEDULER_TIMEZONE = os.getenv("SCHEDULER_TIMEZONE", "America/Manaus")

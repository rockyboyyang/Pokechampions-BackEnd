import os

class Configuration:
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL") or "postgresql://pokebattle_user:H17FrD3!EgQ$@localhost/pokebattle_db"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "klisafluiasdfiuh"
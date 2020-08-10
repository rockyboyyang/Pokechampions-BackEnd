from flask import Flask, request
from flask_migrate import Migrate
from flask_cors import CORS, cross_origin

from app.config import Configuration
from app.routes import users
from app.models import db

app = Flask(__name__)
CORS(app, support_credentials=True)  # this allows us to request info in the backend from the frontend server
# app.config['CORS_HEADERS'] = 'Content-Type'

# def add_cors_headers(response):
#     response.headers['Access-Control-Allow-Origin'] = '*'
#     if request.method == 'OPTIONS':
#         response.headers['Access-Control-Allow-Methods'] = 'DELETE, GET, POST, PUT'
#         headers = request.headers.get('Access-Control-Request-Headers')
#         if headers:
#             response.headers['Access-Control-Allow-Headers'] = headers
#     return response


# app.after_request(add_cors_headers)

app.config.from_object(Configuration)
db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(users.bp)
# app.register_blueprint(trainers.bp)


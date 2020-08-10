from flask import Blueprint, request, jsonify
import jwt
import json
from flask_cors import cross_origin
from werkzeug.security import generate_password_hash

from app.models import db, User
from flask import Response


from ..config import Configuration

bp = Blueprint("session_jobseeker", __name__, url_prefix='/api/session_user')

@bp.route('/', methods=["POST"], strict_slashes=False)
# @cross_origin()
def login():
    data = request.json
    user = User.query.filter(User.username == data['username']).first()
    if not user:
        return {"error": "Email not found"}, 422
    print(data['password'], user.password, generate_password_hash(data['password']))
    if user.check_password(data['password']):
        access_token = jwt.encode({'email': user.username}, Configuration.SECRET_KEY)
        return {'access_token': access_token.decode('UTF-8'), 'user': user.as_dict()}
    else:
        return {"error": "Incorrect password"}, 401
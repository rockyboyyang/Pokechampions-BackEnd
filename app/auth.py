from flask import request
from functools import wraps
import jwt

from app.config import Configuration
from app.models.jobseeker import User


def require_auth_username(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        access_token = request.headers.get('Authorization', None)
        if not access_token:
            return {'error': 'authentication required'}, 401
        try:
            decoded = jwt.decode(access_token, Configuration.SECRET_KEY)
            username = User.query.filter(User.username == decoded.get('username')).first()
        except:
            return {'error': 'invalid auth token'}, 401
        return func(*args, authorized_user=username, **kwargs)
    return wrapped


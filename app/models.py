from flask_sqlalchemy import SQLAlchemy
# from validate_email import validate_email
# import re #i think its a default library
# from ..models import chats, companies, experiences, jobseekers, messages, openings, swipes
from werkzeug.security import generate_password_hash, check_password_hash
# from sqlalchemy_validation import Model, Column

db = SQLAlchemy()


class MixinAsDict:
    def as_dict(self, skip=[]):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns if c.name not in skip}

#for reference
# class MixinGetByUsername:
#     username = Column(String(200), unique=True, nullable=True)
#     @classmethod
#     def get_by_username(cls, username):
#         return session.query(cls).filter(cls.username == username).first()

class User(MixinAsDict, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), nullable=False, unique=True)
    hashed_password = db.Column(db.String(128), nullable=False)
    slot_1 = db.Column(db.String(), nullable=True)
    slot_2 = db.Column(db.String(), nullable=True)
    slot_3 = db.Column(db.String(), nullable=True)
    slot_4 = db.Column(db.String(), nullable=True)
    slot_5 = db.Column(db.String(), nullable=True)
    slot_6 = db.Column(db.String(), nullable=True)
    rank = db.Column(db.String(15), nullable=False)
    boulderbadge = db.Column(db.Boolean, nullable=False)
    cascadebadge = db.Column(db.Boolean, nullable=False)
    thunderbadge = db.Column(db.Boolean, nullable=False)
    rainbowbadge = db.Column(db.Boolean, nullable=False)
    soulbadge = db.Column(db.Boolean, nullable=False)
    marshbadge = db.Column(db.Boolean, nullable=False)
    volcanobadge = db.Column(db.Boolean, nullable=False)
    earthbadge = db.Column(db.Boolean, nullable=False)
    beatElite4_1 = db.Column(db.Boolean, nullable=False)
    beatElite4_2 = db.Column(db.Boolean, nullable=False)
    beatElite4_3 = db.Column(db.Boolean, nullable=False)
    beatElite4_4 = db.Column(db.Boolean, nullable=False)
    beatChampion = db.Column(db.Boolean, nullable=False)

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

    def is_valid_email(self, email):
        # is_valid = validate_email(self.email, check_mx=True)
        return not re.match("[^@]+@[^@]+\.[^@]+", email)

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter(cls.email == email).one()

class Trainer(MixinAsDict, db.Model):
    __tablename__ = 'trainers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    slot_1 = db.Column(db.String(), nullable=False)
    slot_2 = db.Column(db.String(), nullable=False)
    slot_3 = db.Column(db.String(), nullable=False)
    slot_4 = db.Column(db.String(), nullable=False)
    slot_5 = db.Column(db.String(), nullable=False)
    slot_6 = db.Column(db.String(), nullable=False)
    trainerClass = db.Column(db.String(30), nullable=False)
    bio = db.Column(db.Text, nullable=False)
    pre_battle_quote = db.Column(db.Text, nullable=False)
    post_battle_quote = db.Column(db.Text, nullable=False)

        

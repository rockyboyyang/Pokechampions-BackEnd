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


@bp.route('/signup', methods=["POST"])  # create new account
# @cross_origin()
def signup():
    data = request.json
    print(f"\n\n\nDATA\n{data}\n\n\n")
    user = User(
        password=data['password'], 
        username=data['username'], 
        rank='Novice',
        boulderbadge=False,
        cascadebadge=False,
        thunderbadge=False,
        rainbowbadge=False,
        soulbadge=False,
        marshbadge=False,
        volcanobadge=False,
        earthbadge=False,
        beatElite4_1=False,
        beatElite4_2=False,
        beatElite4_3=False,
        beatElite4_4=False,
        beatChampion=False,
    )
    db.session.add(user)
    db.session.commit()

    access_token = jwt.encode(
        {'username': user.username}, Configuration.SECRET_KEY)
    return {'access_token': access_token.decode('UTF-8'), 'user': user.as_dict()}


@bp.route('<int:userId>/edit_pokemon_slot/<string:pokemonSlot>', methods=['PUT'])
def edit_pokemon_user_info(userId, pokemonSlot):
    data = request.json
    user = User.query.filter_by(id=userId).first()

    finStr = str(data).replace("'", '"')
    finStr = finStr.replace("None", "null")
    if 'target"s' in finStr:
        finStr = finStr.replace('target"s', "target's")
    if 'can"t' in finStr:
        finStr = finStr.replace('can"t', "can't")
    if 'hasn"t' in finStr:
        finStr = finStr.replace('hasn"t', "hasn't")
    if 'don"t' in finStr:
        finStr = finStr.replace('don"t', "don't")
    if 'couldn"t' in finStr:
        finStr = finStr.replace('couldn"t', "couldn't")
    if 'won"t' in finStr:
        finStr = finStr.replace('won"t', "won't")
    if 'ner"s' in finStr:
        finStr = finStr.replace('ner"s', "ner's")
    if 'ser"s' in finStr:
        finStr = finStr.replace('ser"s', "ser's")
    if '\n\n' in finStr:
        finStr = finStr.replace('\n\n', " ")


    if pokemonSlot == 'slot_1':
        user.slot_1 = finStr
    if pokemonSlot == 'slot_2':
        user.slot_2 = finStr
    if pokemonSlot == 'slot_3':
        user.slot_3 = finStr
    if pokemonSlot == 'slot_4':
        user.slot_4 = finStr
    if pokemonSlot == 'slot_5':
        user.slot_5 = finStr
    if pokemonSlot == 'slot_6':
        user.slot_6 = finStr


    db.session.commit()

    return { 'user': user.as_dict()}
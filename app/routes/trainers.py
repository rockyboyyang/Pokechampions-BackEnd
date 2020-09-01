from flask import Blueprint, request, jsonify
import jwt
import json
from flask_cors import cross_origin
from werkzeug.security import generate_password_hash

from app.models import db, Trainer
from flask import Response


from ..config import Configuration

bp = Blueprint("gymleaders", __name__, url_prefix='/api/trainers')


@bp.route('/<string:trainerName>')
def fetchTrainerInfo(trainerName):
    
    # handle locked trainers
    trainer = Trainer.query.filter(trainerName == Trainer.name).one().as_dict()
    data = {
        'name': trainer['name'],
        'bio': trainer['bio'],
        'slot_1': trainer['slot_1'],
        'slot_2': trainer['slot_2'],
        'slot_3': trainer['slot_3'],
        'slot_4': trainer['slot_4'],
        'slot_5': trainer['slot_5'],
        'slot_6': trainer['slot_6'],
        'trainerClass': trainer['trainerClass'],
        'pre_battle_quote': trainer['pre_battle_quote'],
        'post_battle_quote': trainer['post_battle_quote'],
    }
    return { 'opponentData': data }



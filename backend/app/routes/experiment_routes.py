from flask import Blueprint, jsonify
from app.models import Experiment

experiment_bp = Blueprint('experiments', __name__)

@experiment_bp.route('/', methods=['GET'])
def get_experiments():
    exps = Experiment.query.all()
    return jsonify([{'id': e.id, 'name': e.name} for e in exps])
from flask import Blueprint

default_bp = Blueprint('default', __name__)

@default_bp.route('/')
def index():
    return "PerturBase API is running."
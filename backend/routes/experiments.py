#!/usr/bin/env python3

from flask import Blueprint, jsonify
from database.db_utils import get_db_connection

experiments_bp = Blueprint('experiments', __name__)

@experiments_bp.route('/', methods=['GET'])
def get_experiments():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Experiment")
    experiments = cursor.fetchall()
    conn.close()
    return jsonify(experiments)
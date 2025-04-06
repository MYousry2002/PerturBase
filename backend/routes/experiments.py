#!/usr/bin/env python3
# backend/routes/experiments.py
from flask import Blueprint, jsonify, request
from database.db_utils import get_db_connection

experiments_bp = Blueprint('experiments', __name__)

@experiments_bp.route('/', methods=['GET'])
def get_experiments():
    # Get query parameters for filtering
    keyword = request.args.get('keyword', '')
    treatment = request.args.get('treatment', '')
    publication = request.args.get('publication', '')
    start_date = request.args.get('start_date', '')
    end_date = request.args.get('end_date', '')

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = "SELECT * FROM Experiment WHERE 1=1"
    params = []

    if keyword:
        query += " AND Name LIKE ?"
        params.append(f"%{keyword}%")
    if treatment:
        query += " AND Treatment = ?"
        params.append(treatment)
    if publication:
        query += " AND Publication = ?"
        params.append(publication)
    if start_date:
        query += " AND Date >= ?"
        params.append(start_date)
    if end_date:
        query += " AND Date <= ?"
        params.append(end_date)

    cursor.execute(query, tuple(params))
    experiments = cursor.fetchall()
    conn.close()
    return jsonify(experiments)


@experiments_bp.route('/advanced', methods=['GET'])
def get_experiments_advanced():
    channel_type = request.args.get('type', '')  # 'RNA', 'sgRNA', 'ADT'
    min_cells = request.args.get('min_cells', 0, type=int)

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Join Experiment with ChannelMetaData to filter based on channel attributes
    query = """
    SELECT DISTINCT e.*
    FROM Experiment e
    JOIN ChannelMetaData cm ON e.ExpID = cm.ExpID
    WHERE 1=1
    """
    params = []

    if channel_type:
        query += " AND cm.Type = ?"
        params.append(channel_type)
    if min_cells:
        query += " AND cm.Ncells >= ?"
        params.append(min_cells)
    
    cursor.execute(query, tuple(params))
    experiments = cursor.fetchall()
    conn.close()
    return jsonify(experiments)


@experiments_bp.route('/<int:exp_id>', methods=['GET'])
def get_experiment(exp_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    cursor.execute("SELECT * FROM Experiment WHERE ExpID = ?", (exp_id,))
    experiment = cursor.fetchone()
    conn.close()
    
    if experiment:
        return jsonify(experiment)
    else:
        return jsonify({"error": "Experiment not found"}), 404
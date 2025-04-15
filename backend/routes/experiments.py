#!/usr/bin/env python3
# backend/routes/experiments.py

from flask import Blueprint, jsonify, request
from ..database.db_utils import get_db_connection

experiments_bp = Blueprint('experiments', __name__)

@experiments_bp.route('/', methods=['GET'])
def get_experiments():
    keyword = request.args.get('keyword', '')
    treatment = request.args.get('treatment', '')
    publication = request.args.get('publication', '')
    start_date = request.args.get('start_date', '')
    end_date = request.args.get('end_date', '')
    exp_type = request.args.get('type', '')
    min_cells = request.args.get('min_cells', type=int)
    source = request.args.get('source', '')
    sort_by = request.args.get('sort_by', 'ExpID')
    sort_order = request.args.get('sort_order', 'ASC').upper()

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Safety: Only allow specific fields for ordering
    allowed_sort_fields = ['ExpID', 'Date']
    allowed_sort_order = ['ASC', 'DESC']

    if sort_by not in allowed_sort_fields:
        sort_by = 'ExpID'
    if sort_order not in allowed_sort_order:
        sort_order = 'ASC'

    query = """
        SELECT
            e.ExpID, e.Name, e.Date, e.Treatment, e.Source, e.Publication,
            MAX(cm.Type) AS Type,
            COUNT(cm.CMID) AS NumChannels,
            SUM(cm.Ncells) AS TotalCells
        FROM Experiment e
        LEFT JOIN ChannelMetaData cm ON e.ExpID = cm.ExpID
        WHERE 1=1
    """
    params = []

    if keyword:
        query += " AND e.Name REGEXP %s"
        params.append(keyword)
    if treatment:
        query += " AND e.Treatment = %s"
        params.append(treatment)
    if publication:
        query += " AND e.Publication = %s"
        params.append(publication)
    if source:
        query += " AND e.Source = %s"
        params.append(source)
    if start_date:
        query += " AND e.Date >= %s"
        params.append(start_date)
    if end_date:
        query += " AND e.Date <= %s"
        params.append(end_date)
    if exp_type:
        query += " AND cm.Type = %s"
        params.append(exp_type)
    if min_cells is not None:
        query += " AND cm.Ncells >= %s"
        params.append(min_cells)

    query += f" GROUP BY e.ExpID ORDER BY e.{sort_by} {sort_order}"

    cursor.execute(query, tuple(params))
    experiments = cursor.fetchall()
    conn.close()
    return jsonify(experiments)


@experiments_bp.route('/distinct_values', methods=['GET'])
def get_distinct_filter_values():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT DISTINCT Treatment FROM Experiment WHERE Treatment IS NOT NULL AND Treatment != ''")
    treatments = sorted([row["Treatment"] for row in cursor.fetchall()])

    cursor.execute("SELECT DISTINCT Source FROM Experiment WHERE Source IS NOT NULL AND Source != ''")
    sources = sorted([row["Source"] for row in cursor.fetchall()])

    conn.close()
    return jsonify({
        "treatments": treatments,
        "sources": sources
    })


@experiments_bp.route('/advanced', methods=['GET'])
def get_experiments_advanced():
    """GET /students_25/Team10/PerturBase/main/api/experiments/advanced"""
    channel_type = request.args.get('type', '')
    min_cells = request.args.get('min_cells', 0, type=int)
    max_mito = request.args.get('max_mito', None)

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
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
    if max_mito is not None:
        query += " AND cm.Mito_avg <= ?"
        params.append(max_mito)
    
    cursor.execute(query, tuple(params))
    experiments = cursor.fetchall()
    conn.close()
    return jsonify(experiments)

@experiments_bp.route('/<int:exp_id>', methods=['GET'])
def get_experiment(exp_id):
    """GET /students_25/Team10/PerturBase/main/api/experiments/<exp_id>"""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM Experiment WHERE ExpID = ?", (exp_id,))
    experiment = cursor.fetchone()
    conn.close()

    if experiment:
        return jsonify(experiment)
    else:
        return jsonify({"error": "Experiment not found"}), 404
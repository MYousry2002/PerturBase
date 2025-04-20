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

    allowed_sort_fields = ['ExpID', 'Date']
    allowed_sort_order = ['ASC', 'DESC']

    if sort_by not in allowed_sort_fields:
        sort_by = 'ExpID'
    if sort_order not in allowed_sort_order:
        sort_order = 'ASC'

    base_query = """
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
        base_query += " AND e.Name REGEXP %s"
        params.append(keyword)
    if treatment:
        base_query += " AND e.Treatment = %s"
        params.append(treatment)
    if publication:
        base_query += " AND e.Publication = %s"
        params.append(publication)
    if source:
        base_query += " AND e.Source = %s"
        params.append(source)
    if start_date:
        base_query += " AND e.Date >= %s"
        params.append(start_date)
    if end_date:
        base_query += " AND e.Date <= %s"
        params.append(end_date)
    if exp_type:
        base_query += " AND cm.Type = %s"
        params.append(exp_type)

    base_query += " GROUP BY e.ExpID"

    # Wrap in subquery if filtering by min_cells
    if min_cells is not None:
        final_query = f"""
            SELECT * FROM ({base_query}) AS subquery
            WHERE subquery.TotalCells >= %s
            ORDER BY subquery.{sort_by} {sort_order}
        """
        params.append(min_cells)
    else:
        final_query = f"{base_query} ORDER BY e.{sort_by} {sort_order}"

    cursor.execute(final_query, tuple(params))
    experiments = cursor.fetchall()
    conn.close()
    return jsonify(experiments)


@experiments_bp.route('/distinct_values', methods=['GET'])
def get_distinct_values():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT DISTINCT Treatment FROM Experiment WHERE Treatment IS NOT NULL")
    treatments = sorted(row["Treatment"] for row in cursor.fetchall())

    cursor.execute("SELECT DISTINCT Source FROM Experiment WHERE Source IS NOT NULL")
    sources = sorted(row["Source"] for row in cursor.fetchall())

    cursor.execute("SELECT DISTINCT Publication FROM Experiment WHERE Publication IS NOT NULL")
    publications_raw = [row["Publication"] for row in cursor.fetchall()]

    # Sort so "Unpublished" always comes first, then other DOIs
    publications = sorted(publications_raw, key=lambda x: (x != "Unpublished", x))

    conn.close()

    return jsonify({
        "treatments": treatments,
        "sources": sources,
        "publications": publications
    })


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
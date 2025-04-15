# backend/routes/dashboard.py
from flask import Blueprint, jsonify
from ..database.db_utils import get_db_connection

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/summary')
def get_summary():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT COUNT(*) FROM Experiment")
    total_experiments = cur.fetchone()[0]

    cur.execute("SELECT COUNT(*) FROM ChannelMetaData")
    total_channels = cur.fetchone()[0]

    cur.execute("SELECT SUM(Ncells) FROM ChannelMetaData")
    total_cells = cur.fetchone()[0] or 0

    cur.execute("SELECT ROUND(AVG(Nfeatures_avg), 1) FROM ChannelMetaData")
    avg_features = cur.fetchone()[0] or 0

    cur.execute("SELECT ROUND(AVG(Mito_avg), 2) FROM ChannelMetaData")
    avg_mito = cur.fetchone()[0] or 0

    cur.execute("SELECT ROUND(AVG(Ribo_avg), 2) FROM ChannelMetaData")
    avg_ribo = cur.fetchone()[0] or 0

    return jsonify({
        "total_experiments": total_experiments,
        "total_channels": total_channels,
        "total_cells": total_cells,
        "avg_features": avg_features,
        "avg_mito": avg_mito,
        "avg_ribo": avg_ribo
    })

@dashboard_bp.route('/cells_by_experiment')
def cells_by_experiment():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT E.Name AS experiment, SUM(C.Ncells) AS total_cells
        FROM Experiment E
        JOIN ChannelMetaData C ON E.ExpID = C.ExpID
        GROUP BY E.Name
    """)
    rows = cur.fetchall()
    return jsonify([dict(zip([col[0] for col in cur.description], row)) for row in rows])

@dashboard_bp.route('/features_by_experiment')
def features_by_experiment():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT E.Name AS experiment, ROUND(AVG(C.Nfeatures_avg), 2) AS avg_features
        FROM Experiment E
        JOIN ChannelMetaData C ON E.ExpID = C.ExpID
        GROUP BY E.Name
    """)
    rows = cur.fetchall()
    return jsonify([dict(zip([col[0] for col in cur.description], row)) for row in rows])

@dashboard_bp.route('/mito_by_channel')
def mito_by_channel():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT CONCAT(E.Name, ' (', C.Type, ')') AS channel, ROUND(C.Mito_avg, 2) AS mito_avg
        FROM ChannelMetaData C
        JOIN Experiment E ON E.ExpID = C.ExpID
    """)
    rows = cur.fetchall()
    return jsonify([dict(zip([col[0] for col in cur.description], row)) for row in rows])

@dashboard_bp.route('/ribo_by_channel')
def ribo_by_channel():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT CONCAT(E.Name, ' (', C.Type, ')') AS channel, ROUND(C.Ribo_avg, 2) AS ribo_avg
        FROM ChannelMetaData C
        JOIN Experiment E ON E.ExpID = C.ExpID
    """)
    rows = cur.fetchall()
    return jsonify([dict(zip([col[0] for col in cur.description], row)) for row in rows])

@dashboard_bp.route('/experiment_type_distribution')
def experiment_type_distribution():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("""
        SELECT Type AS name, COUNT(*) AS count
        FROM ChannelMetaData
        GROUP BY Type
    """)
    rows = cur.fetchall()
    return jsonify([dict(zip([col[0] for col in cur.description], row)) for row in rows])

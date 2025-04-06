#!/usr/bin/env python3
# backend/routes/dashboard.py
from flask import Blueprint, jsonify
from database.db_utils import get_db_connection

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/metrics', methods=['GET'])
def get_dashboard_metrics():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Compute total experiments
    cursor.execute("SELECT COUNT(*) as total FROM Experiment")
    total_experiments = cursor.fetchone()['total']

    # Compute average QC metric (using Mito_avg as an example)
    cursor.execute("SELECT AVG(Mito_avg) as avgQC FROM ChannelMetaData")
    avg_qc = cursor.fetchone()['avgQC']

    # Compute published datasets count (assuming Publication is non-null if published)
    cursor.execute("SELECT COUNT(*) as published FROM Experiment WHERE Publication IS NOT NULL")
    published_count = cursor.fetchone()['published']

    conn.close()

    metrics = {
        "totalExperiments": total_experiments,
        "avgQC": avg_qc,
        "publishedCount": published_count
    }
    return jsonify(metrics)
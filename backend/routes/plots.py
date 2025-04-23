#!/usr/bin/env python3
# backend/routes/plots.py

import os
from flask import Blueprint, jsonify, send_file, current_app
from ..database.db_utils import get_db_connection

plots_bp = Blueprint('plots', __name__)

# Re-declare project root (same logic as in app.py)
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))

@plots_bp.route('/<int:exp_id>/<view_type>', methods=['GET'])
def get_plot_paths(exp_id, view_type):
    """Returns relative API URLs for all plots of a given experiment and view type"""
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    query = """
        SELECT Path
        FROM Figures
        WHERE ExpID = %s AND Type = %s
    """
    cursor.execute(query, (exp_id, view_type))
    figures = cursor.fetchall()
    conn.close()

    # Extract only the filename from the full path stored in DB
    results = []
    for fig in figures:
        full_path = fig["Path"]
        filename = os.path.basename(full_path)
        results.append(f"/api/plots/file/{filename}")

    return jsonify(sorted(results))


@plots_bp.route('/file/<path:filename>', methods=['GET'])
def serve_plot_file(filename):
    """Serves a plot image given a filename extracted from database path"""
    plot_path = os.path.join(project_root, 'backend', 'database', 'plots', filename)

    if not os.path.isfile(plot_path):
        return jsonify({'error': f'File not found: {plot_path}'}), 404

    return send_file(plot_path)
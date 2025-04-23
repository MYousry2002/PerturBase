#!/usr/bin/env python3
# backend/routes/download.py

import os
from flask import Blueprint, send_file, jsonify, current_app
from ..database.db_utils import get_db_connection

download_bp = Blueprint('download', __name__)

@download_bp.route('/rds/<int:exp_id>', methods=['GET'])
def serve_rds_file(exp_id):
    """
    Serves the .rds count matrix file for a given experiment ID.
    Uses the full SeuratPath stored in the database.
    """
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT SeuratPath FROM Experiment WHERE ExpID = %s", (exp_id,))
    row = cursor.fetchone()
    conn.close()

    if not row or not row["SeuratPath"]:
        return jsonify({"error": "Seurat path not found"}), 404

    # Path is already relative to web root — resolve from disk root
    full_path = os.path.join("/var/www/html", row["SeuratPath"].lstrip("/"))

    if not os.path.isfile(full_path):
        return jsonify({"error": f"File does not exist: {full_path}"}), 404

    return send_file(full_path, as_attachment=True)
# backend/routes/dashboard.py

from flask import Blueprint, jsonify

dashboard_bp = Blueprint('dashboard', __name__)

@dashboard_bp.route('/metrics', methods=['GET'])
def get_metrics():
    data = {
        "totalExperiments": 123,
        "avgQC": 0.92,
        "publishedCount": 10
    }
    return jsonify(data)
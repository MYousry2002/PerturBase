from flask import Blueprint, jsonify
from database.db_utils import get_db_connection

raw_counts_bp = Blueprint('raw_counts', __name__)

@raw_counts_bp.route('/', methods=['GET'])
def get_raw_counts():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM RawCounts")
    raw_counts = cursor.fetchall()
    conn.close()
    return jsonify(raw_counts)
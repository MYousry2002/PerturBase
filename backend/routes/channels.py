#!/usr/bin/env python3

from flask import Blueprint, jsonify, request
from database.db_utils import get_db_connection

channels_bp = Blueprint('channels', __name__)

@channels_bp.route('/metadata', methods=['GET'])
def get_channel_metadata():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ChannelMetaData")
    metadata = cursor.fetchall()
    conn.close()
    return jsonify(metadata)

@channels_bp.route('/counts', methods=['GET'])
def get_channel_counts():
    # Optional filtering by feature via query parameter
    feature = request.args.get('feature')
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    if feature:
        query = "SELECT * FROM ChannelCounts WHERE Feature = ?"
        cursor.execute(query, (feature,))
    else:
        cursor.execute("SELECT * FROM ChannelCounts")
    counts = cursor.fetchall()
    conn.close()
    return jsonify(counts)
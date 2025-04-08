#!/usr/bin/env python3
# backend/routes/channels.py

from flask import Blueprint, jsonify, request
from ..database.db_utils import get_db_connection

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

@channels_bp.route('/experiment/<int:exp_id>', methods=['GET'])
def get_channels_for_experiment(exp_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    # Get channel metadata for the experiment
    cursor.execute("SELECT * FROM ChannelMetaData WHERE ExpID = ?", (exp_id,))
    channels = cursor.fetchall()
    conn.close()
    
    return jsonify(channels)
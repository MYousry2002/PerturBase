from flask import Blueprint, jsonify
from database.db_utils import get_db_connection

channels_bp = Blueprint('channels', __name__)

@channels_bp.route('/metadata', methods=['GET'])
def get_channel_metadata():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM ChannelMetaData")
    channels = cursor.fetchall()
    conn.close()
    return jsonify(channels)
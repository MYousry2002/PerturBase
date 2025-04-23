#!/usr/bin/env python3

import mariadb
from ..config import Config  # Import our configuration

def get_db_connection():
    try:
        conn = mariadb.connect(
            host=Config.DB_HOST,
            port=Config.DB_PORT,
            user=Config.DB_USER,
            password=Config.DB_PASSWORD,
            database=Config.DB_NAME
        )
        return conn
    except mariadb.Error as e:
        raise Exception(f"DB connection error: {e}")
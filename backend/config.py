#!/usr/bin/env python3

import os
from dotenv import load_dotenv
from pathlib import Path

# Determine the directory where config.py resides
env_path = Path(__file__).resolve().parent / '.env'
load_dotenv(dotenv_path=env_path)

class Config:
    DB_HOST = os.getenv('DB_HOST')
    if DB_HOST is None:
        raise ValueError("DB_HOST is not set in the environment.")
    
    DB_PORT = os.getenv('DB_PORT')
    if DB_PORT is None:
        raise ValueError("DB_PORT is not set in the environment.")
    DB_PORT = int(DB_PORT)
    
    DB_USER = os.getenv('DB_USER')
    if DB_USER is None:
        raise ValueError("DB_USER is not set in the environment.")
    
    DB_PASSWORD = os.getenv('DB_PASSWORD')
    if DB_PASSWORD is None:
        raise ValueError("DB_PASSWORD is not set in the environment.")
    
    DB_NAME = os.getenv('DB_NAME')
    if DB_NAME is None:
        raise ValueError("DB_NAME is not set in the environment.")
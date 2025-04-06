#!/usr/bin/env python3
import sys
import os

# Add your project directory to the sys.path
project_path = os.path.dirname(os.path.abspath(__file__))
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from app import app as application
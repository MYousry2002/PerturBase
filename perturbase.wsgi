#!/usr/bin/env python3
import sys
import os

project_path = '/var/www/html/students_25/Team10/PerturBase'
if project_path not in sys.path:
    sys.path.insert(0, project_path)

from backend.app import app as application
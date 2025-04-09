#!/usr/bin/env python3
import sys
import os

# Determine the absolute path to the project root
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__)))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Now import your app from the thin wrapper.
from app import app as application
#!/usr/bin/env python3
import sys
import os

# Set the project root
project_root = os.path.abspath(os.path.dirname(__file__))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Import the Flask app from the backend package.
from backend.app import app

if __name__ == "__main__":
    app.run(debug=True)
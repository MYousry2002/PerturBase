#!/usr/bin/env python3

import sys
import os

# Set the absolute project root; adjust this path as needed.
project_root = '/var/www/html/students_25/Team10/PerturBase'
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Now import the app from the backend package.
from backend.app import app

if __name__ == "__main__":
    app.run(debug=True)
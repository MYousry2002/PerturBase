#!/usr/bin/env python3
# main.py — Deployment Ready

import os
import sys

# Ensure the project root is in Python path
project_root = os.path.abspath(os.path.dirname(__file__))
sys.path.insert(0, project_root)

# Standard Flask app import
from backend.app import create_app

app = create_app()
application = app

if __name__ == "__main__":
    app.run(debug=True)

"""
main.py — Development Version
Note: This version avoids using cached modules when updating the Python code (e.g., adding/editing routes).
It's not compatible with standard server deployment (e.g., breaks when server is restarted) — use only for development.

#!/usr/bin/env python3
import importlib.util
import os
import sys

# Clear cached dynamic modules
if "flask_app" in sys.modules:
    del sys.modules["flask_app"]

# Get absolute path to backend/app.py
project_root = os.path.abspath(os.path.dirname(__file__))
app_path = os.path.join(project_root, 'backend', 'app.py')

# Static module name to overwrite consistently
module_name = "flask_app"

# Load backend/app.py dynamically
spec = importlib.util.spec_from_file_location(module_name, app_path)
app_module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(app_module)

# Build the Flask app via the factory pattern
app = app_module.create_app()
application = app

if __name__ == "__main__":
    app.run(debug=True)

"""
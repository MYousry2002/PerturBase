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
application = app  # For server deployment

# Local development server
if __name__ == "__main__":
    app.run(debug=True)
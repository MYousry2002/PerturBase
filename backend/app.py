#!/usr/bin/env python3
import os
import sys
from flask import Flask, send_from_directory
from flask_cors import CORS

# Make sure the project root is added to sys.path.
# This assumes that backend/app.py is located at: <project_root>/backend/app.py
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# Import configuration and routes from the backend package.
from backend.config import Config
from backend.routes import register_routes

# Define the path to the React build folder.
react_build_folder = os.path.join(project_root, 'frontend', 'build')

# Create the Flask application.
# - static_folder is set to the React build folder (which contains index.html and all assets).
# - static_url_path is set to '' so that asset requests like /static/js/... are served correctly.
app = Flask(__name__, static_folder=react_build_folder, static_url_path='')
app.config.from_object(Config)
CORS(app)

# Register API routes (e.g., those defined in backend/routes/__init__.py).
register_routes(app)

# Catch-all route: For any request that doesn’t match an API route or static file,
# serve the React app’s index.html so that client-side routing takes over.
@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    # For local testing; in production this will be run via CGI/WSGI.
    app.run(debug=True)
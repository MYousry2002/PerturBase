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
# Keep static_url_path empty so static file routes work cleanly
app = Flask(__name__, static_folder=react_build_folder, static_url_path='')

# Disable strict slashes to avoid redirect loops between /route and /route/
app.url_map.strict_slashes = False

app.config.from_object(Config)
CORS(app)

# Register API routes (e.g., those defined in backend/routes/__init__.py).
register_routes(app)

# Serve static files manually so React Router works with nested paths
@app.route('/students_25/Team10/PerturBase/main', defaults={'path': ''})
@app.route('/students_25/Team10/PerturBase/main/<path:path>')
def serve_react(path):
    # Serve static assets (JS, CSS) if they exist
    full_path = os.path.join(app.static_folder, path)
    if path != "" and os.path.exists(full_path):
        return send_from_directory(app.static_folder, path)
    # Otherwise serve the React index.html for frontend routes
    return send_from_directory(app.static_folder, 'index.html')

# Optional: fallback for 404s to index.html (can be removed if above works fine)
@app.errorhandler(404)
def not_found(e):
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    # For local testing; in production this will be run via CGI/WSGI.
    app.run(debug=True)
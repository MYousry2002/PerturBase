#!/usr/bin/env python3
import os
import sys
from flask import Flask, send_from_directory
from flask_cors import CORS

# 1. Ensure the project root is on sys.path.
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

# 2. Import your config and route-registration
from backend.config import Config
from backend.routes import register_routes

# 3. Path to the React build folder
react_build_folder = os.path.join(project_root, 'frontend', 'build')

# 4. Create the Flask application, using the React build folder for static files
app = Flask(__name__, static_folder=react_build_folder, static_url_path='')

# 5. Configure app settings & CORS
app.config.from_object(Config)
CORS(app)

# 6. Disable strict slash
app.url_map.strict_slashes = False

# 7. Register all routes (the API Blueprints)
register_routes(app)

# 8. Fallback route to serve the React app.
#    This handles all requests under "/students_25/Team10/PerturBase/main"
#    that are not matched by an API route or an existing file.
@app.route('/students_25/Team10/PerturBase/main', defaults={'path': ''})
@app.route('/students_25/Team10/PerturBase/main/<path:path>')
def serve_react(path):
    # Check if the requested file actually exists in build/...
    full_path = os.path.join(app.static_folder, path)
    if path and os.path.exists(full_path):
        # Serve the static file (e.g. JS, CSS, images)
        return send_from_directory(app.static_folder, path)
    
    # Otherwise, serve index.html so React Router can handle the path in the frontend
    return send_from_directory(app.static_folder, 'index.html')

# 9. (Optional) A 404 handler that also serves index.html
@app.errorhandler(404)
def not_found(e):
    # Usually, for unknown routes, just let React handle it
    return send_from_directory(app.static_folder, 'index.html')

if __name__ == "__main__":
    # For local testing (in production, you'd use WSGI / mod_wsgi / gunicorn)
    app.run(debug=True)
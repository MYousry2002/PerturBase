# backend/factory.py

import os
from flask import Flask, send_from_directory
from flask_cors import CORS
from backend.config import Config
from backend.routes import register_routes

def create_app():
    """
    Flask application factory.
    Creates and configures a new Flask app instance.
    """

    # Resolve the root of the project
    project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

    # Define path to React build (static frontend)
    react_build_folder = os.path.join(project_root, 'frontend', 'build')

    # Initialize Flask app with React static folder
    app = Flask(
        __name__,
        static_folder=react_build_folder,
        static_url_path=''
    )

    # Apply configuration and enable CORS
    app.config.from_object(Config)
    CORS(app)

    # Optional: ignore trailing slashes in routes
    app.url_map.strict_slashes = False

    # Register all backend routes (e.g. via Blueprints)
    register_routes(app)

    @app.route('/_factory_reloaded')
    def factory_reloaded():
        return "latest version loaded of PerturBase!"

    # Route: Serve React index.html or static files
    @app.route('/students_25/Team10/PerturBase/main', defaults={'path': ''})
    @app.route('/students_25/Team10/PerturBase/main/<path:path>')
    def serve_react(path):
        """
        Serves static assets from the React build folder.
        If the file doesn't exist, return index.html for React Router to handle.
        """
        full_path = os.path.join(app.static_folder, path)
        if path and os.path.exists(full_path):
            return send_from_directory(app.static_folder, path)
        return send_from_directory(app.static_folder, 'index.html')

    # Global 404 fallback (also serves index.html for unknown routes)
    @app.errorhandler(404)
    def not_found(e):
        """
        Handles unmatched routes and errors by serving React index.html.
        Enables SPA routing from the frontend.
        """
        return send_from_directory(app.static_folder, 'index.html')

    return app
#!/usr/bin/env python3
import os
import sys
import importlib.util

# Detect environment: development vs production
if os.getenv('APP_ENV') == 'development':
    # Development logic
    """
    Development mode: avoids using cached modules, 
    enables automatic reload when updating backend code (routes, configs, etc.).
    Not compatible with server restarts — intended for local development only.
    """

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

    # Build the Flask app via factory
    app = app_module.create_app()
    application = app

    if __name__ == "__main__":
        app.run(debug=True)

else:
    # Production logic
    """
    Production mode: standard import for server deployment.
    Compatible with server restarts.
    """

    # Ensure the project root is in Python path
    project_root = os.path.abspath(os.path.dirname(__file__))
    if project_root not in sys.path:
        sys.path.insert(0, project_root)

    # Standard import
    from backend.app import create_app

    app = create_app()
    application = app  # WSGI entrypoint

    if __name__ == "__main__":
        # Only for manual testing locally
        app.run(debug=False)
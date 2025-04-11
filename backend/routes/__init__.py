#!/usr/bin/env python3
# backend/routes/__init__.py

from .experiments import experiments_bp
from .channels import channels_bp
from .raw_counts import raw_counts_bp
from .dashboard import dashboard_bp

def register_routes(app):
    # Use a prefix that matches your domain structure:
    # e.g. "/students_25/Team10/PerturBase/main/api"
    # Then your routes become:
    #   /students_25/Team10/PerturBase/main/api/experiments
    #   /students_25/Team10/PerturBase/main/api/channels
    #   etc.

    app.register_blueprint(experiments_bp, url_prefix='/students_25/Team10/PerturBase/main/api/experiments')
    app.register_blueprint(channels_bp,    url_prefix='/students_25/Team10/PerturBase/main/api/channels')
    app.register_blueprint(raw_counts_bp,  url_prefix='/students_25/Team10/PerturBase/main/api/raw_counts')
    app.register_blueprint(dashboard_bp,   url_prefix='/students_25/Team10/PerturBase/main/api/dashboard')

    print("Routes have been registered.")
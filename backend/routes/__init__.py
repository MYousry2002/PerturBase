#!/usr/bin/env python3
# backend/routes/__init__.py

from .experiments import experiments_bp
from .channels import channels_bp
from .raw_counts import raw_counts_bp
from .dashboard import dashboard_bp
from .plots import plots_bp

def register_routes(app):
    
    app.register_blueprint(experiments_bp, url_prefix='/api/experiments')
    app.register_blueprint(channels_bp,    url_prefix='/api/channels')
    app.register_blueprint(raw_counts_bp,  url_prefix='/api/raw_counts')
    app.register_blueprint(dashboard_bp,   url_prefix='/api/dashboard')
    app.register_blueprint(plots_bp,       url_prefix='/api/plots')

    print("Routes have been registered.")
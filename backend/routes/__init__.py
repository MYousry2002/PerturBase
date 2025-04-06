#!/usr/bin/env python3

# backend/routes/__init__.py
from .default import default_bp
from .experiments import experiments_bp
from .channels import channels_bp
from .raw_counts import raw_counts_bp
from .dashboard import dashboard_bp

def register_routes(app):
    app.register_blueprint(default_bp)  # Root route
    app.register_blueprint(experiments_bp, url_prefix='/experiments')
    app.register_blueprint(channels_bp, url_prefix='/channels')
    app.register_blueprint(raw_counts_bp, url_prefix='/raw_counts')
    app.register_blueprint(dashboard_bp, url_prefix='/dashboard')
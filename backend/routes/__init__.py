from flask import Blueprint
from .experiments import experiments_bp
from .channels import channels_bp
from .raw_counts import raw_counts_bp

def register_routes(app):
    app.register_blueprint(experiments_bp, url_prefix='/api/experiments')
    app.register_blueprint(channels_bp, url_prefix='/api/channels')
    app.register_blueprint(raw_counts_bp, url_prefix='/api/raw_counts')
#!/usr/bin/env python3

from .default import default_bp
from .experiments import experiments_bp
from .channels import channels_bp
from .raw_counts import raw_counts_bp

def register_routes(app):
    app.register_blueprint(default_bp)
    app.register_blueprint(experiments_bp, url_prefix='/experiments')
    app.register_blueprint(channels_bp, url_prefix='/channels')
    app.register_blueprint(raw_counts_bp, url_prefix='/raw_counts')
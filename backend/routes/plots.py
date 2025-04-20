#!/usr/bin/env python3
# backend/routes/plots.py
import os
from flask import Blueprint, jsonify, current_app

plots_bp = Blueprint('plots', __name__)

@plots_bp.route('/<exp_id>/<view_type>', methods=['GET'])
def get_plot_images(exp_id, view_type):
    # Points to build/plots inside the frontend
    plots_dir = os.path.join(current_app.static_folder, 'plots')
    prefix = f"{exp_id}_{view_type.lower().replace(' ', '_')}"
    matching = []

    try:
        for fname in os.listdir(plots_dir):
            if fname.startswith(prefix) and fname.endswith(".png"):
                matching.append(f"/plots/{fname}")
    except FileNotFoundError:
        return jsonify([])

    return jsonify(sorted(matching))
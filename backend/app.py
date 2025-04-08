#!/usr/bin/env python3

from flask import Flask
from .config import Config
from flask_cors import CORS
from .routes import register_routes

app = Flask(__name__)
app.config.from_object(Config)
CORS(app)

# Initialize routes (Blueprints)
register_routes(app)

if __name__ == "__main__":
    app.run(debug=True)
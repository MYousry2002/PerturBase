#!/bin/bash
# Script to run the app in either development or production mode
# Usage: ./run-app.sh development | production

MODE="$1"

if [ "$MODE" == "development" ]; then
    echo "Launching app in development mode (dynamic reload enabled)..."
    export APP_ENV=development
elif [ "$MODE" == "production" ]; then
    echo "Launching app in production mode..."
    export APP_ENV=production
else
    echo "Error: Please specify 'development' or 'production' as an argument."
    echo "Example: ./run-app.sh development"
    echo "         ./run-app.sh production"
    exit 1
fi
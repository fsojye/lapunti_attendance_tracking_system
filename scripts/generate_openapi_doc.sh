#!/bin/bash

APP_DIR="utils"
OUTPUT_DIR="docs"
OUTPUT_FILE="openapi.json"

PYTHON_PATH="$(pwd)/.venv/bin/python"

mkdir -p $OUTPUT_DIR

$PYTHON_PATH -m $APP_DIR.generate_openapi_doc > $OUTPUT_DIR/openapi.json

echo "Generated OpenAPI doc at $OUTPUT_DIR/$OUTPUT_FILE"

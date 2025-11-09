#!/bin/bash

APP_DIR="src"

uv pip install -r $APP_DIR/requirements.txt \
    --require-hashes

#!/bin/bash

APP_DIR="src"

uv pip compile $APP_DIR/requirements.in -o $APP_DIR/requirements.txt \
    --generate-hashes

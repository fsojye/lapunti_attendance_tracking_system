#!/bin/bash

APP_DIR="src"

uv pip compile $APP_DIR/requirements.in -o $APP_DIR/requirements.txt \
    --generate-hashes \
    --no-cache-dir \
    --no-header \
    --no-emit-index-url \
    --emit-build-options \
    --strip-extras

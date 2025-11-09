#!/bin/bash

APP_DIR="src"

uvicorn main:app --reload --app-dir=${APP_DIR}
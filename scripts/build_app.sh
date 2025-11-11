#!/bin/bash
set -euo pipefail

ACTION=${1:-}

if [ -z "$ACTION" ] || [[ ! "$ACTION" =~ ^(check|fix)$ ]]; then
  echo "Usage: $0 <check|fix>"
  exit 1
fi

APP_DIR="src"

echo "Type checking python code"
mypy $APP_DIR --config-file $APP_DIR/pyproject.toml

if [[ "$ACTION" == "check" ]]; then
  echo "Format checking python code"
  ruff check  $APP_DIR --config $APP_DIR/pyproject.toml
fi

if [[ "$ACTION" == "fix" ]]; then
  echo "Formatting python code"
  ruff check  $APP_DIR --config $APP_DIR/pyproject.toml --fix
  ruff format  $APP_DIR --config $APP_DIR/pyproject.toml
fi

if [[ $? -ne 0 ]]; then
  echo "Formatting issues found"
  exit $?
fi
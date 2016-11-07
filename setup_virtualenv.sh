#!/bin/sh

set -e

# Default to using python3
python=$(command -v python3)

if ! command -v virtualenv >/dev/null 2>/dev/null
then
  echo "No virtualenv found in your path, so can't set it up."
  exit 1
fi

if test -d venv
then
  echo "The venv directory already exists, so nothing to do."
  return 2
fi

virtualenv -p $python venv

echo "=== virtualenv setup complete ==="
echo "Now, activate the environment."

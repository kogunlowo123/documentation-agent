#!/bin/bash
set -euo pipefail
echo "Setting up Documentation Agent..."
pip install -e ".[dev]"
echo "Setup complete!"

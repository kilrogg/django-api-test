#!/bin/bash
set -ex

##
## Create some aliases
##

# Convenience workspace directory for later use
WORKSPACE_DIR=$(pwd)

echo 'export PATH="/home/developer/.local/bin:$PATH"' >> ~/.bashrc

# Change some Poetry settings to better deal with working in a container
poetry config cache-dir ${WORKSPACE_DIR}/.cache
poetry config virtualenvs.in-project true

# Now install all dependencies
poetry install

echo "Done!"

#!/bin/sh -l

# If any steps below errors, fail the script immediately.
set -e

SERVER_ADDRESS="${1}:${2}"
API_KEY=${3}
WORKFLOW_PATH=${4}

python3 /install_aqueduct.py -s ${SERVER_ADDRESS}  -a ${API_KEY}

# Temporary hack to restrict cryptography to version that's before 38.0.0
# We should enforce this in our main package instead.
pip3 install "cryptography<38.0.0"

AQUEDUCT_SERVER_ADDRESS=${SERVER_ADDRESS} AQUEDUCT_API_KEY=${API_KEY} python3 ${WORKFLOW_PATH}
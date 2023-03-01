#!/bin/bash

# Helper script only meant to be run from Makefile

set -eu

DIRECTORY=$1
shift
echo "Running $@ inside $DIRECTORY without Docker"

cd "$DIRECTORY" && exec "$@"

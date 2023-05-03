#!/usr/bin/env bash

# Helper script only meant to be run from Makefile

set -eu

DIRECTORY=$1
shift
echo "Running $@ inside $DIRECTORY in Docker"

docker run -v "$PWD:/app" -w "/app/$DIRECTORY" -ti ctf-lessons-latex "$@"

#!/bin/sh

set -eu

export TFC_TOKEN="$1"
export TFC_ORGANIZATION="$2"
export TFC_CLIENT_NAME="$3"
export GH_ORGANIZATION="$4"
export GH_REPOSITORY="$5"

python main.py

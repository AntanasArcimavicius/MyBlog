#!/bin/bash
set -eux pipefail

# BUILD WEB:
make build

# TEST WEB:
docker-compose run web "make" "migrate" "testall"

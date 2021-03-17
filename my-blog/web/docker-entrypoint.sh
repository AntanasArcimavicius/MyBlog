#!/bin/bash
# https://github.com/ufoscout/docker-compose-wait
export WAIT_HOSTS="$MB_DB_HOST:$MB_DB_PORT"
/wait
# https://github.com/krallin/tini
tini -- $@
#!/bin/bash
# https://github.com/ufoscout/docker-compose-wait
export WAIT_HOSTS="$SA_DB_HOST:$SA_DB_PORT"
/wait
# https://github.com/krallin/tini
tini -- $@
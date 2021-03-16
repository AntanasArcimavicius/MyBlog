#!/usr/bin/env bash

set -ueo pipefail

# Convert space-delimited string to array
DOMAINS=(${MB_SSL_DOMAINS:-example.org})
DOMAIN="${DOMAINS[0]}"
export NGINX_DOMAIN="${DOMAIN}"

BASE_PATH=/etc/letsencrypt
DOMAIN_PATH=$BASE_PATH/live/$DOMAIN

if [ ! -f "$DOMAIN_PATH/privkey.pem" ]; then
  echo "### Creating dummy certificate for $DOMAIN ..."

  mkdir -p "$DOMAIN_PATH"

  openssl req -x509 -nodes -newkey rsa:1024 -days 1 \
    -keyout "$DOMAIN_PATH/privkey.pem" \
    -out "$DOMAIN_PATH/fullchain.pem" \
    -subj '/CN=localhost'

  touch $DOMAIN_PATH/.dummy-cert
fi

# API service that reloads nginx on request
htpasswd -bc /tmp/.htpasswd "${MB_NGINX_API_USER}" "${MB_NGINX_API_PASSWORD}" > /dev/null 2>&1
(
  while true ; do
    {
      echo -e "HTTP/1.1 200 OK\n\nNGINX reload requested at: $(date)"
      nginx -s reload &
    } | nc -l -p 9000 -q 1
  done
) &

# Original entrypoint for nginx
exec /nginx-entrypoint.sh "$@"

# syntax = docker/dockerfile:1.1-experimental
# The above line ensures BuildKit is used if it's enabled via DOCKER_BUILDKIT=1
# environment variable. If the environment variable is not present, it has no
# effect as of Docker 19.03.

ARG BASE_IMAGE=python:3.8-slim-buster
ARG BUILDER=builder

#############
# Stage: zero
#############

FROM ${BASE_IMAGE} as zero

ENV DEBIAN_FRONTEND=noninteractive
ENV PYTHONFAULTHANDLER=true

# Below will create media and static folders as root
ARG MB_STATIC_ROOT
ARG MB_MEDIA_ROOT
ENV MB_STATIC_ROOT=${MB_STATIC_ROOT}
ENV MB_MEDIA_ROOT=${MB_MEDIA_ROOT}

WORKDIR ${MB_STATIC_ROOT}
WORKDIR ${MB_MEDIA_ROOT}

RUN useradd --create-home user
RUN chown user: ${MB_STATIC_ROOT} ${MB_MEDIA_ROOT}
RUN echo "root:root" | chpasswd

###############
# Stage: system
###############

FROM zero AS system

RUN apt-get -y update && apt-get -y upgrade \
 && apt-get install -y --no-install-recommends \
    postgresql-client \
    tini \
    sudo \
    mime-support \
 && apt-get -y clean && rm -rf /var/lib/apt/lists/*

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.7.3/wait /wait
RUN chmod +x /wait

COPY docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

###################
# Stage: dev-system
###################

FROM system AS dev-system

RUN apt-get -y update \
 && apt-get install -y --no-install-recommends \
    sqlite3 libsqlite3-dev \
    make \
    vim \
    shared-mime-info

#####################
# Stage: requirements
#####################

FROM zero AS requirements

RUN apt-get -y update && apt-get -y upgrade \
 && apt-get install -y --no-install-recommends \
    build-essential \
 && apt-get -y clean && rm -rf /var/lib/apt/lists/*

COPY requirements*.txt ./
RUN python3 -m venv /venv \
 && /venv/bin/pip install --upgrade pip==20.2.4 \
 && /venv/bin/pip install -r requirements.txt

#########################
# Stage: dev-requirements
#########################

FROM requirements AS dev-requirements

RUN  /venv/bin/pip install -r requirements-dev.txt

################
# Stage: builder
################

FROM zero AS builder

COPY --from=system / /
COPY --from=requirements --chown=user:user /venv /venv

####################
# Stage: dev-builder
####################

FROM zero AS dev-builder

COPY --from=dev-system / /
COPY --from=dev-requirements --chown=user:user /venv /venv

# Install integration testing dependecies
# Uncomment when there will be tests
#COPY install-packages-for-test.sh ./
#RUN ./install-packages-for-test.sh

USER user 

# Download browser binaries for e2e testing
# Uncomment when there will be tests
#RUN /venv/bin/python -m playwright install

#############
# Stage: code
#############

FROM ${BUILDER} AS code

WORKDIR /app/web

# Run as non-root
USER user

# Copy the source code
COPY . .

# Instead of installing the app in --editable mode
# we install it into site-packages and symlink the code.
# Otherwise the python egg (mb.egg-info) gets clobbered
# when mounting the code on to the docker container.
RUN /venv/bin/pip install . \
 && rm -rf /venv/lib/python3.8/site-packages/mb \
 && ln -s /app/web/mb /venv/lib/python3.8/site-packages/

# Activate virtualenv (for convenience)
ENV PATH=/venv/bin:$PATH VIRTUAL_ENV=/venv

STOPSIGNAL SIGINT

ENTRYPOINT ["/docker-entrypoint.sh"]

RUN django collectstatic --noinput

CMD ["/venv/bin/uwsgi", "--ini", "/app/web/uwsgi.ini"]

############
# Stage: dev
############

FROM code AS dev

#############
# Stage: prod
#############

FROM code AS prod

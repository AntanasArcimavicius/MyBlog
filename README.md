This project has been built from cookiecutter template

imports: isort    /  code style: black /
security: bandit /   linter: pylint


build the docker images:
make /
Install pre-commit hooks:
make pre-commit

Makefile shorthands for common commands:

make up         # Run app

make pdb        # Run app with pdb debugger support

make ssh        # Log into the web container

make lint       # Run pre-commit on all files 

make test       # Run tests

make reset_db   # Reset current db

Inside the container, the app is installed inside a virtualenv located in /venv.
The venv is automatically activated for you.

Configuration
Default configuration values are located in the .env file (not included in git) is automatically loaded when
running docker-compose, and the values contained in it are available for interpolation in docker-compose.yml
To override configuration modify docker-compose.override.yml, this file is .gitignored.
See docker-compose documentation for details: https://docs.docker.com/compose/extends/

Testing
This uses pytest and pytest-django.
Configuration is in pytest.ini. Run tests from inside the web container with pytest.

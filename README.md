# Delta Sync
Delta-based synchronization demo web application made with FastAPI, SocketIO (TMEXIO), SQLAlchemy, React & Vite

## Backend
### Install
```sh
pip install poetry==2.1.3
poetry --directory=backend install
pre-commit install
```

If you are using PyCharm, mark the `backend` directory as "Sources Root"

### Run
```sh
docker compose up -d --wait
```

## Frontend
```sh
cd frontend
```

### Run (dev-mode)
```sh
npm run develop
```

### Build
```sh
npm run build
```

## Additions
### Docker
Here is a template dockerfile for python /w poetry:
```dockerfile
FROM python:3.13-alpine

# TODO change to any directory
WORKDIR /app
RUN pip install --upgrade pip

# TODO set to your poetry version
RUN pip install poetry==2.1.3
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-interaction --no-ansi --only main

# TODO `COPY` your project files

# TODO set the ENTRYPOINT and/or CMD
```

### Docker Compose
And a template docker-compose file:
```yaml
services:
  app:
    # depends_on:
    #   database: 
    #     condition: service_healthy
    build:
      context: .
      dockerfile: Dockerfile
    # image:
    restart: always
    # command: ...
    # ports:
    #   - target: 8000
    #     host_ip: 127.0.0.1
    #     published: 8000
    # volumes:
    #   - type: bind  # TODO you can pass source files for hot-reloading
    #     source: <SOURCE>
    #     target: /<WORKDIR>
    # environment:
    #   SECRET: local
```

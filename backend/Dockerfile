FROM xieffect/python-base:python-3.13-poetry-2.1.3

WORKDIR /backend
COPY pyproject.toml poetry.lock ./
RUN poetry install --no-interaction --no-ansi --only main

COPY app ./app

ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0"]

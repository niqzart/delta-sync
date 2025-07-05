FROM python:3.13-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /backend

RUN pip install poetry==2.1.3
RUN poetry config virtualenvs.create false

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-interaction --no-ansi --only main

COPY app ./app

ENTRYPOINT ["uvicorn", "app.main:app", "--host", "0.0.0.0"]

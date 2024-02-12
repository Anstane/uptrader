FROM python:3.11-slim
WORKDIR /app
RUN pip install poetry==1.6.1
COPY poetry.lock pyproject.toml ./
RUN poetry install --no-interaction --no-ansi
COPY . ./
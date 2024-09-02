FROM python:3.12
WORKDIR /tg_message_bot
COPY ../pyproject.toml .
RUN pip install poetry && poetry install --no-root
COPY app/ .
CMD ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
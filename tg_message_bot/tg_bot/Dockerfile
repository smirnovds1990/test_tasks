FROM python:3.12
WORKDIR /tg_message_bot
COPY ../pyproject.toml .
RUN pip install poetry && poetry install --no-root
COPY tg_bot/ .
CMD ["poetry", "run", "python", "./bot.py"]
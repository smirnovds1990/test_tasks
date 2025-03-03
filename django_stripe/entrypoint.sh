#!/bin/sh
uv run manage.py migrate --noinput
uv run manage.py shell << EOF
from django.contrib.auth.models import User
User.objects.create_superuser('user', '', '123qwe123qwe')
EOF
uv run manage.py runserver ${HOST}:${PORT}

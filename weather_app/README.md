# Weather App
Приложение для просмотра погоды в разных городах. Пользователь вводит название города и получает почасовую сводку погоды на ближайшее время.

Технологии:
[![Python](https://skillicons.dev/icons?i=py,django,docker&theme=dark)](https://skillicons.dev/)
___
### Использование

**Docker**
```sh
git clone https://github.com/smirnovds1990/weather_app.git
cd weather_app
touch .env
# Добавить нужные переменные в .env-файл (смотреть .env.example)
docker compose up
# Перейти на 0.0.0.0:8000
```
**pip**
```sh
git clone https://github.com/smirnovds1990/weather_app.git
cd weather_app
python -m venv venv
source venv/bin/activate (Windows - source venv/Scripts/activate)
touch .env
# Добавить нужные переменные в .env-файл (смотреть .env.example)
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
# Перейти на 127.0.0.1:8000
```
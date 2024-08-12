FROM python:3.12
WORKDIR /weather_app
COPY ./requirements.txt /weather_app/
RUN pip install -r requirements.txt --no-cache-dir
COPY . /weather_app/
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
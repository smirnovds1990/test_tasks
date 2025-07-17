# fastapi_ai_bot
Этот API, позволяет загружать .jpg/.png файл и проверяет его на содержание небезопасного/нежелательного(nsfw) контента.

##### Использование:
Установите виртуальное окружение и зависимости:
```bash
python3 -m venv venv  # Для Windows: python
source venv/bin/activate  # Для Windows: python source venv/Scripts/activate
pip install -r requirements.txt
```

Зарегистрируйтесь на https://jigsawstack.com/ чтобы получить API-ключ
Создайте в корневой директории .env-файл и в нем переменную API_KEY=, как указано в .env.example

Запустите сервер:
```bash
fastapi dev main.py
```

Проверка файла:
```bash
# Перейдите http://127.0.0.1:8000/docs
# Откройте доступный эндпоинт — "/moderate"
# Нажмите кнопку "Try it out"
# Загрузите изображение, нажмите "Execute"
# Ниже, в разделе "Responses" вы увидите ответ
```

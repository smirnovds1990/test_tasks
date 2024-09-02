import os
from urllib.parse import urljoin

from dotenv import load_dotenv


load_dotenv()


TOKEN = os.getenv('TOKEN', 'token')
# BASE_URL = 'http://127.0.0.1:8000/'
BASE_URL = 'http://backend:8000/'
GET_MESSAGES_URL = urljoin(BASE_URL, 'api/v1/messages/')
CREATE_MESSAGE_URL = urljoin(BASE_URL, 'api/v1/message/')

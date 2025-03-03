import os

from dotenv import load_dotenv


load_dotenv()

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = os.getenv("REDIS_PORT")
BASE_REDIS_URL = os.getenv("BASE_REDIS_URL")
TELEGRAM_BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
API_URL = os.getenv("API_URL")
AUTH_API_TOKEN = os.getenv("AUTH_API_TOKEN")
START_MESSAGE = "Send me an IMEI to check its validity."
WHITELIST = "whitelist"
NOT_AUTHORAZIED_MESSAGE = "You are not authorized to use this bot."
IMEI_REGEX = r"^\d{8,15}$"
INVALID_IMEI_VALIDATION_MESSAGE = (
    "Invalid IMEI. It should be from 8 to 15 symbols long and "
    "contain only digits."
)
IMEI_IS_VALID_MESSAGE = "IMEI is valid!\nDetails:\n"
IMEI_IS_INVALID_MESSAGE = "IMEI is invalid!\nMessage:\n"
IMEI_REQUEST_FAILED_MESSAGE = "Request of IEMI is failed. Please try again."

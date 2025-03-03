import os

from dotenv import load_dotenv


load_dotenv()

AUTH_API_TOKEN = os.getenv("AUTH_API_TOKEN")
IMEICHECK_API_TOKEN = os.getenv("IMEICHECK_API_TOKEN")
IMEICHECK_SERVICE_ID = os.getenv("IMEICHECK_SERVICE_ID")
IMEICHECK_API_URL = os.getenv("IMEICHECK_API_URL")
API_ERROR_MESSAGE = "IMEI Check API Error"

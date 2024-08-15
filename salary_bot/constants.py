import os

from dateutil.rrule import DAILY, HOURLY, MONTHLY
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.getenv('TOKEN')
DATABASE_URI = os.getenv('DATABASE_URI')
GROUP_TYPES = {
    'hour': {
        "year": {"$year": "$dt"},
        "month": {"$month": "$dt"},
        "day": {"$dayOfMonth": "$dt"},
        "hour": {"$hour": "$dt"}
    },
    'day': {
        "year": {"$year": "$dt"},
        "month": {"$month": "$dt"},
        "day": {"$dayOfMonth": "$dt"}
    },
    'month': {
        "year": {"$year": "$dt"},
        "month": {"$month": "$dt"}
    }
}
PERIOD_ITEMS = {
    'hour': HOURLY,
    'day': DAILY,
    'month': MONTHLY
}
DATETIME_FORMAT = '%Y-%m-%dT%H:%M:%S'
DATA_FORMAT_EXAMPLE = {
        "dt_from": "2022-09-01T00:00:00",
        "dt_upto": "2022-12-31T23:59:00",
        "group_type": "month"
    }

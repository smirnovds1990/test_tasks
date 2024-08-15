from aiogram import Bot, Dispatcher
from motor import motor_asyncio

from constants import DATABASE_URI, TOKEN


bot = Bot(token=TOKEN)
dp = Dispatcher()
client = motor_asyncio.AsyncIOMotorClient(DATABASE_URI)
db = client.salaries.salaries

from motor import motor_asyncio

from constants import DATABASE_URL


client = motor_asyncio.AsyncIOMotorClient(DATABASE_URL)
db = client.get_database('bot_messages')
collection = db.get_collection('messages')

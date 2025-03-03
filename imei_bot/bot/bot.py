import asyncio

from aiogram import Bot, Dispatcher
from dotenv import load_dotenv

from constants import TELEGRAM_BOT_TOKEN
from handlers import main_router


load_dotenv()
bot = Bot(token=TELEGRAM_BOT_TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(main_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

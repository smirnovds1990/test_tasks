import asyncio

from aiogram import Bot, Dispatcher

from constants import TOKEN
from handlers import main_router


bot = Bot(TOKEN)
dp = Dispatcher()


async def main():
    dp.include_router(main_router)
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

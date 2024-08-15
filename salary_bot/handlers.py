import json

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from constants import DATA_FORMAT_EXAMPLE, PERIOD_ITEMS
from utils import (
    get_data_from_db, get_period_of_time, pack_data_to_message,
    parse_data_from_message
)


main_router = Router()


@main_router.message(CommandStart())
async def start_command(message: Message):
    if message.from_user is None:
        await message.answer('Не удалось получить информацию о пользователе.')
        return

    if (
        message.from_user.first_name is None or
        message.from_user.last_name is None
    ):
        await message.answer(f'Привет {message.from_user.username}')
    else:
        await message.answer(
            f'Привет {message.from_user.first_name} '
            f'{message.from_user.last_name}'
        )
    await message.answer(
        f'Для получения данных пришли сообщение в формате: '
        f'{DATA_FORMAT_EXAMPLE}'
    )


@main_router.message()
async def get_dataset(message: Message):
    try:
        start, stop, group_type = parse_data_from_message(message.text)
        period = get_period_of_time(
            start=start, stop=stop, period_item=PERIOD_ITEMS[group_type]
        )
        dataset, labels = await get_data_from_db(
            start=start, stop=stop, group_type=group_type, period=period
        )
        result = pack_data_to_message(dataset=dataset, labels=labels)
        await message.answer(result)
    except json.JSONDecodeError:
        await message.answer(
            'Некорректный формат. Отправьте данные в JSON-формате.'
        )

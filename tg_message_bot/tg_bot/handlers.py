from aiogram import F, Router
from aiohttp import ClientSession
from aiogram.filters import CommandStart
from aiogram.fsm.context import FSMContext
from aiogram.types import (
    KeyboardButton, Message, ReplyKeyboardMarkup,
)

from constants import CREATE_MESSAGE_URL, GET_MESSAGES_URL
from states import MessageState


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
    buttons = [
        [
            KeyboardButton(text='Получить все сообщения'),
            KeyboardButton(text='Написать сообщение'),
        ]
    ]
    keyboard = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True,
        one_time_keyboard=True
    )
    await message.answer(
        'Выберите одно из действий, доступных в кнопках.',
        reply_markup=keyboard
    )


@main_router.message(F.text == 'Получить все сообщения')
async def get_messages(message: Message):
    async with ClientSession() as session:
        response = await session.get(GET_MESSAGES_URL)
        all_messages = await response.json(encoding='utf-8')
        await message.answer(
            text=f'Ваши сообщения: {all_messages}',
        )


@main_router.message(F.text == 'Написать сообщение')
async def get_message_text(message: Message, state: FSMContext):
    await message.answer('Введите сообщение:')
    await state.set_state(MessageState.waiting_for_message)


@main_router.message(MessageState.waiting_for_message)
async def send_message(message: Message, state: FSMContext):
    user_message = message.text
    payload = {'text': user_message, 'author': message.from_user.username}
    async with ClientSession() as session:
        response = await session.post(CREATE_MESSAGE_URL, json=payload)
        await message.answer(f'{await response.text(encoding='utf-8')}')
        await state.clear()

import re

from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

from constants import (
    IMEI_REGEX,
    INVALID_IMEI_VALIDATION_MESSAGE,
    NOT_AUTHORAZIED_MESSAGE,
    START_MESSAGE,
    WHITELIST,
)
from redis_client import redis_client
from utils import (
    form_response_from_request_result, process_request_to_imei_api
)


main_router = Router()


@main_router.message(CommandStart())
async def send_welcome(message: Message):
    """Handle /start command."""
    await message.answer(START_MESSAGE)


@main_router.message()
async def check_imei_handler(message: Message):
    """Handle IMEI validation, request to IMEI API and response to a user."""
    if not (
        await redis_client.sismember(WHITELIST, message.from_user.username)
    ):
        await message.answer(NOT_AUTHORAZIED_MESSAGE)
        return
    else:
        imei = message.text.strip()
        if not re.fullmatch(IMEI_REGEX, imei):
            await message.answer(INVALID_IMEI_VALIDATION_MESSAGE)
            return
        response = await process_request_to_imei_api(imei)
        answer = await form_response_from_request_result(response)
        await message.answer(answer)

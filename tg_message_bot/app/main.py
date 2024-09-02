from contextlib import asynccontextmanager
from collections.abc import AsyncIterator

from fastapi import Body, FastAPI, Response
from fastapi_cache import FastAPICache
from fastapi_cache.backends.redis import RedisBackend
from fastapi_cache.decorator import cache
from http import HTTPStatus
from redis import asyncio as aioredis

from db import collection
from models import BaseMessage, MessagesList


@asynccontextmanager
async def lifespan(_: FastAPI) -> AsyncIterator[None]:
    # redis = aioredis.from_url("redis://localhost")
    redis = aioredis.from_url("redis://redis")
    FastAPICache.init(RedisBackend(redis), prefix="fastapi-cache")
    yield


app = FastAPI(lifespan=lifespan)


# Under the comments is a pagination template
# It's not deceided how to send page and page_size from the bot
@app.get(
    '/api/v1/messages/',
)
@cache(expire=3600, namespace='messages')
async def get_all_messages(
    response: Response
    # page: int = 1,
    # page_size: int = 10
):
    # skip = (page - 1) * page_size
    # items = (
    #     await collection.find().skip(skip).limit(page_size).to_list(page_size)
    # )
    # total_items = await collection.count_documents({})
    # messages_list = {
    #     'items': MessagesList(messages=items),
    #     'total': total_items,
    #     'page': page,
    #     'page_size': page_size,
    #     'total_pages': (total_items + page_size - 1) // page_size
    # }
    # return messages_list
    response.headers["Cache-Control"] = (
        "no-store, no-cache, must-revalidate, max-age=0"
    )
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return MessagesList(messages=await collection.find().to_list(None))


@app.post(
    '/api/v1/message/',
    response_model=BaseMessage,
    status_code=HTTPStatus.CREATED,
    response_model_by_alias=False
)
async def create_message(message: BaseMessage = Body()):
    new_message = await collection.insert_one(
        message.model_dump(by_alias=True, exclude=['id'])
    )
    await FastAPICache.clear(namespace='messages')
    created_message = await collection.find_one(
        {'_id': new_message.inserted_id}
    )
    return created_message

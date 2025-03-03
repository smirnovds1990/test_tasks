from redis import asyncio as aioredis

from utils import get_redis_url


redis_client = aioredis.from_url(get_redis_url())

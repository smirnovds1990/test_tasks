import httpx
from httpx import codes, Response

from constants import (
    API_URL,
    AUTH_API_TOKEN,
    BASE_REDIS_URL,
    IMEI_IS_INVALID_MESSAGE,
    IMEI_IS_VALID_MESSAGE,
    IMEI_REQUEST_FAILED_MESSAGE,
    REDIS_HOST,
    REDIS_PORT,
)


def get_redis_url() -> str:
    return f"{BASE_REDIS_URL}{REDIS_HOST}:{REDIS_PORT}"


async def process_request_to_imei_api(imei: str) -> Response:
    async with httpx.AsyncClient() as client:
        return await client.post(
            url=API_URL,
            json={"imei": imei, "token": AUTH_API_TOKEN},
        )


async def form_response_from_request_result(response: Response) -> str:
    """Get a response from IMEI API and form a message according to it."""
    if response.status_code == codes.OK:
        data = response.json()
        if data.get("status") == "successful":
            return f"{IMEI_IS_VALID_MESSAGE}{data}"
        else:
            return f"{IMEI_IS_INVALID_MESSAGE}{data.get("errors")}"
    else:
        return IMEI_REQUEST_FAILED_MESSAGE

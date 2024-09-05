import asyncio

from constants import CONNECTIONS_AMOUNT
from server_logger import server_logger
from utils import tcp_client, start_server


async def main():
    """Запуск сервера и отправка запросов."""
    server_task = asyncio.create_task(start_server())

    # Задержка, чтобы сервер успел запуститься
    await asyncio.sleep(1)

    clients = [
        asyncio.create_task(tcp_client(i)) for i in range(CONNECTIONS_AMOUNT)
    ]
    await asyncio.gather(*clients)
    server_task.cancel()
    try:
        await server_task
    except asyncio.CancelledError:
        server_logger.info('Сервер остановлен')


asyncio.run(main())

import asyncio
import random

from constants import BYTES_TO_READ, HOST, MAX_INTERVAL, MIN_INTERVAL, PORT
from server_logger import server_logger


async def handle_client(reader, writer):
    """Callback для обработки подключений к серверу."""
    addr = writer.get_extra_info('peername')
    server_logger.info(f'Подключен клиент: {addr}')
    try:
        while True:
            data = await reader.read(BYTES_TO_READ)
            if not data:
                break
            message = data.decode()
            server_logger.info(f'Получено сообщение от {addr}: {message}')
            writer.write(data)
            await writer.drain()
    except asyncio.CancelledError:
        server_logger.info('Отменено клиентом')
    finally:
        server_logger.info(f'Отключен клиент: {addr}')
        writer.close()
        await writer.wait_closed()


async def start_server():
    """Реализация подключения к серверу."""
    server = await asyncio.start_server(handle_client, HOST, PORT)
    addr = server.sockets[0].getsockname()
    server_logger.info(f'Сервер запущен на {addr}')
    try:
        async with server:
            await server.serve_forever()
    except asyncio.CancelledError:
        server_logger.info('Завершение работы сервера.')


async def tcp_client(client_id):
    """Реализация подключения клиента к серверу."""
    reader, writer = await asyncio.open_connection(HOST, PORT)
    server_logger.info(f'Клиент {client_id} подключен к серверу')
    for i in range(5):
        await asyncio.sleep(random.randint(MIN_INTERVAL, MAX_INTERVAL))
        message = f'Сообщение {i+1} от клиента {client_id}'
        writer.write(message.encode())
        await writer.drain()
        data = await reader.read(BYTES_TO_READ)
        server_logger.info(f'Клиент {client_id} получил эхо: {data.decode()}')
    server_logger.info(f'Клиент {client_id} завершает работу')
    writer.close()
    await writer.wait_closed()

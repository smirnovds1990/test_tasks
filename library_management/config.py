import argparse
from typing import Iterable


def configure_parser(actions: Iterable[str]) -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description='Управление библиотекой')
    parser.add_argument(
        'actions', choices=actions, help='Доступные действия'
    )
    parser.add_argument('--id', help='ID книги')
    parser.add_argument('--title', help='Название')
    parser.add_argument('--author', help='Автор')
    parser.add_argument('--year', help='Год')
    parser.add_argument(
        '--status', help='Статус', choices=['В наличии', 'Выдана']
    )
    return parser

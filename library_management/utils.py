import json
import os

from constants import DATA_URL


def initialize_json_data_file() -> None:
    """Создает файл для данных, если его нет."""
    if not os.path.exists(DATA_URL):
        with open(DATA_URL, 'w', encoding='utf-8') as file:
            json.dump([], file, ensure_ascii=False, indent=4)


def load_data_from_data_file() -> list[dict[str, int | str]]:
    """Загружает данные из файла или отдает пустой список, если файл пуст."""
    with open(DATA_URL, 'r', encoding='utf-8') as file:
        try:
            return json.load(file)
        except json.JSONDecodeError:
            print('Библиотека пуста.')
            return []


def get_max_id() -> int:
    """Получает максимальный id для формирования следующего."""
    data = load_data_from_data_file()
    all_ids = [int(book['id']) for book in data]
    return max(all_ids)


def save_data_to_file(data: list) -> None:
    """Сохраняет данные в файл."""
    with open(DATA_URL, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

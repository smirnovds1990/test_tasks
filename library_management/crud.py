import json

from utils import (
    get_max_id, initialize_json_data_file, load_data_from_data_file,
    save_data_to_file
)


def add_book(title: str, author: str, year: str) -> str:
    initialize_json_data_file()
    data = load_data_from_data_file()
    if not data:
        data = []
        new_id = 1
    else:
        titles = [book['title'] for book in data]
        if title in titles:
            return f'Книга "{title}" уже есть в библиотеке.'
        max_id = get_max_id()
        new_id = max_id + 1
    new_data = {
        'id': new_id,
        'title': title,
        'author': author,
        'year': year,
        'status': 'В наличии'
    }
    data.append(new_data)
    save_data_to_file(data)
    return (
        'Успешно добавлена новая книга:'
        f' {json.dumps(new_data, ensure_ascii=False)}'
    )


def delete_book(id: int) -> str:
    data = load_data_from_data_file()
    if not data:
        return 'Библиотека пуста'
    renewed_data = [book for book in data if book['id'] != int(id)]
    deleted_book = [book for book in data if book['id'] == int(id)]
    if not deleted_book:
        return f'Книги с id = {id} нет в библиотеке.'
    save_data_to_file(renewed_data)
    return (
        'Успешно удалена книга:'
        f' {json.dumps(deleted_book, ensure_ascii=False)}'
    )


def get_book(
        title: str | None = None,
        author: str | None = None,
        year: str | None = None
) -> list[dict[str, int | str]] | str:
    data = load_data_from_data_file()
    if title:
        wanted_books = [
            book for book in data if book['title'] == title
        ]
        if not wanted_books:
            return f'Книги с названием {title} нет в библиотеке.'
    if author:
        wanted_books = [
            book for book in data if book['author'] == author
        ]
        if not wanted_books:
            return f'Книги с автором {author} нет в библиотеке.'
    if year:
        wanted_books = [
            book for book in data if book['year'] == year
        ]
        if not wanted_books:
            return f'Книги с годом {year} нет в библиотеке.'
    return wanted_books


def get_all_books() -> list[dict[str, int | str]]:
    return load_data_from_data_file()


def change_book_status(id: int, status: str) -> str:
    data = load_data_from_data_file()
    wanted_book = [book for book in data if book['id'] == int(id)]
    if not wanted_book:
        return f'Книги с id = {id} нет в библиотеке.'
    another_books = [book for book in data if book['id'] != int(id)]
    if wanted_book[0]['status'] != status:
        wanted_book[0]['status'] = status
        another_books.append(wanted_book[0])
        save_data_to_file(another_books)
        return (
            f'Статус {wanted_book[0]["title"]} успешно изменен на "{status}".'
        )
    else:
        return 'Запрашиваемая книга уже находится в переданном статусе.'

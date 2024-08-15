from config import configure_parser
from crud import (
    add_book, change_book_status, delete_book, get_all_books, get_book
)


ACTIONS = {
    'add': add_book,
    'delete': delete_book,
    'find': get_book,
    'get_all': get_all_books,
    'change_status': change_book_status
}


def main() -> None:
    parser = configure_parser(ACTIONS.keys())
    args = parser.parse_args()
    func_kwargs = {}
    if args.id:
        func_kwargs['id'] = args.id
    if args.title:
        func_kwargs['title'] = args.title
    if args.author:
        func_kwargs['author'] = args.author
    if args.year:
        func_kwargs['year'] = args.year
    if args.status:
        func_kwargs['status'] = args.status
    try:
        result = ACTIONS[args.actions](**func_kwargs)
    except KeyError as error:
        print(f'Ошибка: {error}. Неизвестный режим работы: {args.actions}')
    if result:
        print(result)


if __name__ == '__main__':
    main()

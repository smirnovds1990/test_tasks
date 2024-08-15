import os
import unittest

from constants import DATA_URL
from crud import (
    add_book, change_book_status, delete_book, get_all_books, get_book
)
from utils import (
    get_max_id, initialize_json_data_file, load_data_from_data_file,
    save_data_to_file
)


class InitializeFileTests(unittest.TestCase):

    def test_initialize_json_data_file(self):
        file_exists = os.path.exists(DATA_URL)
        self.assertFalse(file_exists)
        initialize_json_data_file()
        file_exists = os.path.exists(DATA_URL)
        self.assertTrue(file_exists)


class UtilsTests(unittest.TestCase):

    test_data = [
            {'id': 1, 'title': 'test1'},
            {'id': 2, 'title': 'test2'},
            {'id': 3, 'title': 'test3'},
            {'id': 4, 'title': 'test4'}
        ]

    def setUp(self):
        initialize_json_data_file()

    def tearDown(self):
        os.remove(DATA_URL)

    def test_load_data_from_data_file_with_empty_file(self):
        self.assertEqual(load_data_from_data_file(), [])

    def test_data_saves_to_file_and_loads_from_it(self):
        save_data_to_file(self.test_data)
        self.assertEqual(load_data_from_data_file(), self.test_data)

    def test_get_max_id(self):
        save_data_to_file(self.test_data)
        self.assertEqual(get_max_id(), 4)


class AddDeleteTests(unittest.TestCase):

    test_data = {'title': 'test', 'author': 'test_author', 'year': '1990'}

    def tearDown(self):
        os.remove(DATA_URL)

    def test_add_book(self):
        add_book(**self.test_data)
        added_book = load_data_from_data_file()
        self.assertEqual(added_book[0]['title'], self.test_data['title'])
        self.assertEqual(added_book[0]['author'], self.test_data['author'])
        self.assertEqual(added_book[0]['year'], self.test_data['year'])

    def test_delete_book(self):
        initialize_json_data_file()
        self.assertEqual(len(load_data_from_data_file()), 0)
        add_book(**self.test_data)
        self.assertEqual(len(load_data_from_data_file()), 1)
        delete_book(1)
        self.assertEqual(len(load_data_from_data_file()), 0)


class GetChangeStatusTests(unittest.TestCase):

    test_data = {'title': 'test', 'author': 'test_author', 'year': '1990'}

    def setUp(self):
        add_book(**self.test_data)

    def tearDown(self):
        os.remove(DATA_URL)

    def test_get_book_by_title(self):
        wanted_books = get_book(title='test')
        self.assertEqual(wanted_books[0]['title'], 'test')  # type: ignore

    def test_get_book_by_author(self):
        wanted_books = get_book(author='test_author')
        self.assertEqual(
            wanted_books[0]['author'], 'test_author'  # type: ignore
        )

    def test_get_book_by_year(self):
        wanted_books = get_book(year='1990')
        self.assertEqual(wanted_books[0]['year'], '1990')  # type: ignore

    def test_get_book_with_wrong_title(self):
        wrong_title = 'wrong_title'
        wanted_books = get_book(title=wrong_title)
        expected = f'Книги с названием {wrong_title} нет в библиотеке.'
        self.assertEqual(wanted_books, expected)

    def test_get_book_with_wrong_author(self):
        wrong_author = 'wrong_author'
        wanted_books = get_book(author=wrong_author)
        expected = f'Книги с автором {wrong_author} нет в библиотеке.'
        self.assertEqual(wanted_books, expected)

    def test_get_book_with_wrong_year(self):
        wrong_year = 'wrong_author'
        wanted_books = get_book(year=wrong_year)
        expected = f'Книги с годом {wrong_year} нет в библиотеке.'
        self.assertEqual(wanted_books, expected)

    def test_change_book_status(self):
        current_data = load_data_from_data_file()
        current_status = current_data[0]['status']
        self.assertEqual(current_status, 'В наличии')
        change_book_status(id=1, status='Выдана')
        current_data = load_data_from_data_file()
        current_status = current_data[0]['status']
        self.assertEqual(current_status, 'Выдана')


class GetAllBooksTests(unittest.TestCase):

    test_data = [
            {'title': 'test1', 'author': 'test_author1', 'year': '1990'},
            {'title': 'test2', 'author': 'test_author2', 'year': '1990'},
            {'title': 'test3', 'author': 'test_author3', 'year': '1990'},
        ]

    def tearDown(self):
        os.remove(DATA_URL)

    def test_get_all_books(self):
        initialize_json_data_file()
        all_books = get_all_books()
        self.assertEqual(len(all_books), 0)
        for book in self.test_data:
            add_book(**book)
        all_books = get_all_books()
        self.assertEqual(len(all_books), 3)

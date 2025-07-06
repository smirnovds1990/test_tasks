import unittest
from parsel import Selector

from solution import WikiSpider


class TestWikiSpider(unittest.TestCase):

    def setUp(self):
        self.spider = WikiSpider()

    def test_count_first_letters(self):
        html = """
        <div id="mw-pages">
            <div class="mw-category-group">
                <ul>
                    <li><a href="/wiki/Акула">Акула</a></li>
                    <li><a href="/wiki/Бобр">Бобр</a></li>
                    <li><a href="/wiki/Бабочка">Бабочка</a></li>
                    <li><a href="/wiki/Собака">Собака</a></li>
                    <li><a href="/wiki/Deer">Deer</a></li>
                    <li><a href="/wiki/Cat">Cat</a></li>
                </ul>
            </div>
        </div>
        """
        expected_result = {"А": 1, "Б": 2, "С": 1}
        selector = Selector(text=html)
        html_element = selector.css("div#mw-pages div.mw-category-group ul li")
        self.spider.count_first_letters(html_element=html_element)
        self.assertEqual(self.spider.letters_counter, expected_result)

    def test_get_total_results(self):
        self.spider.letters_counter = {"А": 3, "В": 5, "Е": 10, "П": 5}
        expected_result = [
            {"letter": "А", "count": 3},
            {"letter": "В", "count": 5},
            {"letter": "Е", "count": 10},
            {"letter": "П", "count": 5},
        ]
        self.assertEqual(
            list(self.spider.get_total_results()), expected_result
        )


if __name__ == "__main__":
    unittest.main()

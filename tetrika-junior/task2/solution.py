import re
from collections import defaultdict

import scrapy
from scrapy.crawler import CrawlerProcess


class WikiSpider(scrapy.Spider):
    name = "wiki_spider"
    start_urls = [
        "https://ru.wikipedia.org/wiki/Категория:Животные_по_алфавиту"
    ]

    def __init__(self):
        self.letters_counter = defaultdict(int)

    def count_first_letters(self, html_element):
        for item in html_element:
            first_letter = item.css("a::text").get()[:1]
            if re.match(r"^[А-Яа-яЁё]$", first_letter):
                self.letters_counter[first_letter] += 1

    def get_total_results(self):
        for letter, count in self.letters_counter.items():
            yield {"letter": letter, "count": count}

    def parse(self, response):
        self.count_first_letters(
            response.css("div#mw-pages div.mw-category-group ul li")
        )
        next_page = response.xpath(
            "//a[text()='Следующая страница']/@href"
        ).get()
        if next_page:
            yield response.follow(next_page, callback=self.parse)
        else:
            yield from self.get_total_results()


if __name__ == "__main__":
    crawler_process = CrawlerProcess(
        settings={
            "FEEDS": {
                "beasts.csv": {
                    "format": "csv",
                    "overwrite": True,
                }
            }
        },
    )
    crawler_process.crawl(WikiSpider)
    crawler_process.start()

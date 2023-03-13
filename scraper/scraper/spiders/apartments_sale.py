import scrapy

from scraper.items import ScraperItem


class ApartmentsSaleSpider(scrapy.Spider):
    LIMIT = 500
    name = 'apartments_sale'
    allowed_domains = ['www.sreality.cz']
    start_urls = [
        f"https://www.sreality.cz/api/en/v2/estates?category_main_cb=1&category_type_cb=1&per_page={LIMIT}",
    ]

    def parse(self, response):
        data = response.json()
        for estate in data["_embedded"]["estates"]:
            item = ScraperItem()
            item["title"] = estate["name"]
            item["image_url"] = estate["_links"]["images"][0]["href"]
            yield item


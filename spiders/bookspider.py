import scrapy
from bookscraper.items import BookItem
import random
from urllib.parse import urlencode


# gets the url fo the site we want to scrape, encode it, and return
def get_proxy_url(url):
    payload = {'api_key': 'bde06357-2f15-406f-a106-49b78b544469', 'url': url}
    proxy_url = 'https://proxy.scrapeops.io/v1/?' + urlencode(payload)
    return proxy_url


class BookspiderSpider(scrapy.Spider):
    name = "bookspider"
    allowed_domains = ["books.toscrape.com", "https://proxy.scrapeops.io/v1/"]
    start_urls = ["https://books.toscrape.com/"]

    custom_settings = {
        'FEEDS': {
            'booksdata.csv': {'format': 'csv', 'overwrite': True},
        }
    }

    def start_requests(self):
        yield scrapy.Request(url=get_proxy_url(self.start_urls[0]), callback=self.parse)

    user_agent_list = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 14_4_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.0.3 Mobile/15E148 Safari/604.1',
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36 Edg/87.0.664.75',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.18363',
]

    def parse(self, response):
        books = response.css("article.product_pod")
        for book in books:
            relative_url = book.css("h3 a ::attr(href)").get()

            if "catalogue/" in relative_url:
                book_url = "https://books.toscrape.com/" + relative_url
            else:
                book_url = "https://books.toscrape.com/catalogue/" + relative_url
            yield scrapy.Request(url=get_proxy_url(book_url), callback=self.parse_book_page, meta={"proxy": "http://user-asdas3a4545:12345678@gate.smartproxy.com:7000"})

        next_page = response.css("li.next a ::attr(href)").get()
        if next_page is not None:
            if "catalogue/" in next_page:
                next_page_url = "https://books.toscrape.com/" + next_page
            else:
                next_page_url = "https://books.toscrape.com/catalogue/" + next_page
            yield scrapy.Request(url=get_proxy_url(next_page_url), callback=self.parse, meta={"proxy": "http://user-asdas3a4545:12345678@gate.smartproxy.com:7000"})

    def parse_book_page(self, response):

        table_rows = response.css("table tr")
        book_item = BookItem()

        book_item["url"] = response.url,
        book_item["title"] = response.css(".product_main h1::text").get(),
        book_item["upc"] = table_rows[0].css("td ::text").get(),
        book_item["product_type"] = table_rows[1].css("td ::text").get(),
        book_item["price_excl_tax"] = table_rows[2].css("td ::text").get(),
        book_item["price_incl_tax"] = table_rows[3].css("td ::text").get(),
        book_item["tax"] = table_rows[4].css("td ::text").get(),
        book_item["availability"] = table_rows[5].css("td ::text").get(),
        book_item["num_reviews"] = table_rows[6].css("td ::text").get(),
        book_item["stars"] = response.css("p.star-rating").attrib["class"],
        book_item["category"] = response.xpath("//ul[@class='breadcrumb']/li[@class='active']/preceding-sibling::li[1]/a/text()").get(),
        book_item["description"] = response.xpath("//div[@id='product_description']/following-sibling::p/text()").get(),
        book_item["price"] = response.css("p.price_color ::text").get(),

        yield book_item

import csv
import scrapy
from scrapy.exceptions import CloseSpider

class SvetnewparsSpider(scrapy.Spider):
    name = "svetnewpars"
    allowed_domains = ["divan.ru"]
    start_urls = ["https://www.divan.ru/ekaterinburg/category/svet"]

    def __init__(self, *args, **kwargs):
        super(SvetnewparsSpider, self).__init__(*args, **kwargs)
        self.csvfile = open('svet.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.csvfile)

    def closed(self, reason):
        self.csvfile.close()

    def parse(self, response):
        svetilniks = response.css('div._Ud0k')
        for svetilnik in svetilniks:
            name = svetilnik.css('div.lsooF span::text').get()
            price = svetilnik.css('div.pY3d2 span::text').get()
            url = svetilnik.css('a::attr(href)').get()
            self.writer.writerow([name, price, url])

        # Ищем ссылки на все страницы
        next_pages = response.css('a.PaginationLink::attr(href)').getall()
        if next_pages:
            for next_page in next_pages:
                abs_url = response.urljoin(next_page)
                yield response.follow(abs_url, callback=self.parse)
        else:
            raise CloseSpider('Все страницы спарсены')
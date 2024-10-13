import scrapy

class SvetnewparsSpider(scrapy.Spider):
    name = "svetnewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/ekaterinburg/category/svet"]

    def parse(self, response):
        svetilniks = response.css('div._Ud0k')
        for svetilnik in svetilniks:
            yield {
            'name' : svetilniks.css('div.lsooF span::text').get(),
            'price' : svetilniks.css('div.pY3d2 span::text').get(),
            'url' : svetilniks.css('a').attrib['href']
            }

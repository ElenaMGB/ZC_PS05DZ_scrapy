import scrapy

class SvetnewparsSpider(scrapy.Spider):
    name = "svetnewpars"
    allowed_domains = ["https://divan.ru"]
    start_urls = ["https://www.divan.ru/ekaterinburg/category/svet"]

    def parse(self, response):
        svetilniks = response.css('div._Ud0k')
        for svetilnik in svetilniks:
            yield {
            'name': svetilnik.css('div.lsooF span::text').get(),
            'price': svetilnik.css('div.pY3d2 span::text').get(),
            'url': svetilnik.css('a::attr(href)').get()
            # 'url' : svetilniks.css('a').attrib['href'] изменено по совету сети
            }

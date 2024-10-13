**Тема 7- Парсинг. Введение в scrapy. WEB-scraping**

**Задание**

Попробуй написать spider для нахождения всех источников освещения с сайта divan.ru

Нужно взять название источника освещения, цену и ссылку

*Можно попробовать сделать это на другом сайте с продажей источников освещения

В поле для ответа загрузи ссылку на Git.

**Решение**
Выгрузка данных в csv file командой 
scrapy crawl svetnewpars -o svet.csv


**Старое решение**
для выгрузки полученных данных в json-формат （svet.json) код дополнен по следующей инструкции

Для того, чтобы сохранить результаты парсинга в файле svet.json, вам нужно использовать специальный экспортер в Scrapy, который называется JsonItemExporter. Вот как это можно сделать:

    Создайте новый файл pipelines.py в том же каталоге, где находится ваш SvetnewparsSpider.

    В файле pipelines.py добавьте следующий код:

import json

class SvetJsonPipeline:
    def __init__(self):
        self.file = open('svet.json', 'wb')

    def process_item(self, item, spider):
        line = json.dumps(dict(item), ensure_ascii=False) + "\n"
        self.file.write(line.encode('utf-8'))
        return item

    def spider_closed(self, spider):
        self.file.close()

Этот код определяет новый класс SvetJsonPipeline, который открывает файл svet.json в режиме записи байтов (wb) и сохраняет каждый элемент (item) в этот файл в формате JSON. Метод spider_closed закрывает файл после завершения работы паука.

    В файле settings.py добавьте новую строку в список ITEM_PIPELINES:

ITEM_PIPELINES = {
    'YOUR_PROJECT_NAME.pipelines.SvetJsonPipeline': 300,
}

Замените YOUR_PROJECT_NAME на имя вашего проекта Scrapy.

    Измените метод parse в SvetnewparsSpider следующим образом:

def parse(self, response):
    svetilniks = response.css('div._Ud0k')
    for svetilnik in svetilniks:
        yield {
            'name': svetilnik.css('div.lsooF span::text').get(),
            'price': svetilnik.css('div.pY3d2 span::text').get(),
            'url': svetilnik.css('a::attr(href)').get()
        }

Обратите внимание на изменения в способе получения URL (svetilnik.css('a::attr(href)').get()).

После этих изменений, когда вы запустите паука, результаты парсинга будут сохранены в файле svet.json в том же каталоге, где находится ваш проект Scrapy.
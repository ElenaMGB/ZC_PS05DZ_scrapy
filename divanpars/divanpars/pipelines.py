# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DivanparsPipeline:
    def process_item(self, item, spider):
        return item

# import json

# class SvetJsonPipeline:
#     def __init__(self):
#         self.file = open('svet.json', 'wb')

#     def process_item(self, item, spider):
#         line = json.dumps(dict(item), ensure_ascii=False) + "\n"
#         self.file.write(line.encode('utf-8'))
#         return item

    def spider_closed(self, spider):
        self.file.close()
# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

import json

from Tencent.dao.BaLoLTiebaDao import BaLoLTiebaDao
from Tencent.dao.BaPositionDao import BaPositonDao


class TencentPipeline(object):

    def __init__(self):
        self.f = open("tencent.json", "w")
        self.baPositionDao = BaPositonDao()
        self.baLoLTiebaDao = BaLoLTiebaDao()

    def process_item(self, item, spider):
        if spider.name == 'tencent':
            content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
            self.f.write(content)
            # self.baPositionDao.saveItem(item)

        elif spider.name == 'lol':
            #content = json.dumps(dict(item), ensure_ascii=False) + ",\n"
           # self.f.write(content)
            self.baLoLTiebaDao.saveItem(item)
        return item
    def close_spider(self, spider):
        self.f.close()



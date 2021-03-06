# -*- coding: utf-8 -*-
import scrapy

from Tencent.dao.BaUrlDao import BaUrlDao
from Tencent.items import TencentItem, LoLItem, TiebaUrlItem, BaUrlItem


class BaUrlSpider(scrapy.Spider):
    # 爬虫名
    name = 'baUrl'
    # 爬虫爬取数据的域范围
    allowed_domains = ['www.qidian.com']
    # 1. 需要拼接的url
    baseURL = "https://vipreader.qidian.com/chapter/1014215189/467624775"
    # 1. 需要拼接的url地址的偏移量
    offset = 0
    # 爬虫启动时，读取的url地址列表
    start_urls = [baseURL]

    def __init__(self):
        self.baseUrlDao = BaUrlDao()
        self.dealedItems = set()
        self.visitedUrl = set()
        self.visitedUrl.add(self.baseURL)

    # 用来处理response
    def parse(self, response):
        # 提取每个response的数据
        node_list = []
        try:
            node_list =  response.xpath("//a")
        except:
            print "not support content"
            node_list = []

        for node in node_list:
            href = node.xpath('@href')
            urlDesc = node.xpath('text()')

            if len(href) > 0 :
                hrefStr =  href.extract()[0].encode("utf-8")
                urlDescStr = ''

                if hrefStr not in self.visitedUrl:
                    self.visitedUrl.add(hrefStr);
                    if len(urlDesc) > 0:
                        urlDescStr = urlDesc.extract()[0].encode("utf-8")

                    if hrefStr.find("qidian.com") != -1 or hrefStr.startswith("//"):

                        if hrefStr.startswith("//") :
                            hrefStr = "https:"+hrefStr
                        item = BaUrlItem()
                        item['relativeType'] = 1
                        item['url'] = hrefStr
                        item['baseUrl'] = "https://www.qidian.com/"
                        item['urlDesc'] = urlDescStr
                        yield item
                    elif hrefStr.startswith('/'):
                        item = BaUrlItem()
                        item['relativeType'] = 2
                        item['url'] = hrefStr
                        item['baseUrl'] = "https://www.qidian.com/"
                        item['urlDesc'] = urlDescStr
                        yield item


        # 第一种写法：拼接url，适用场景：页面没有可以点击的请求连接，必须通过拼接url才能获取响应
        # if self.offset < 2190:
        #     self.offset += 10
        #     url = self.baseURL + str(self.offset)
        #     yield scrapy.Request(url, callback = self.parse)


        # 第二种写法：直接从response获取需要爬取的连接，并发送请求处理，直到链接全部提取完
        # if len(response.xpath("//a[contains(@class,'next')]")) > 0:
        #
        #     url = response.xpath("//a[contains(@class,'next')]/@href").extract()[0]
        #     yield scrapy.Request("http:" + url, callback = self.parse)

        item =  self.baseUrlDao.getOneItem()
        if len(item) > 0  :
            url = item['url']
            if item['relativeType'] == 2:
                url = item['baseUrl'] + item['url']
            self.baseUrlDao.dealUsedItem(item)

            if url not in self.dealedItems  :
                self.dealedItems.add(url)
                yield scrapy.Request(url, callback=self.parse,dont_filter = True)


    #def parse_next(self, response):
    #    pass






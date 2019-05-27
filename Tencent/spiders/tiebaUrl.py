# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem, LoLItem, TiebaUrlItem


class TiebaUrlSpider(scrapy.Spider):
    # 爬虫名
    name = 'tiebaUrl'
    # 爬虫爬取数据的域范围
    allowed_domains = ['tieba.baidu.com']
    # 1. 需要拼接的url
    baseURL = "http://tieba.baidu.com/f/index/forumpark?pcn=%E6%B8%B8%E6%88%8F&pci=0&ct=1&rn=20&pn=1"
    # 1. 需要拼接的url地址的偏移量
    offset = 0
    # 爬虫启动时，读取的url地址列表
    start_urls = [baseURL + str(offset)]

    # 用来处理response
    def parse(self, response):
        # 提取每个response的数据
        node_list = response.xpath("//div[@id='ba_list']/div")

        for node in node_list:
            print node.attrib['class']
            if 'ba_info' in node.attrib['class']:
                # 构建item对象，用来保存数据
                item = TiebaUrlItem()
                # 提取每个职位的信息，并且将提取出的Unicode字符串编码为UTF-8编码
                item['title'] = 'game'
                item['url'] = node.xpath("./a//@href").extract()[0].encode("utf-8")

                item['name'] = node.xpath("./a/div/p[@class='ba_name']/text()").extract()[0].encode("utf-8")

                yield item

        # 第一种写法：拼接url，适用场景：页面没有可以点击的请求连接，必须通过拼接url才能获取响应
        # if self.offset < 2190:
        #     self.offset += 10
        #     url = self.baseURL + str(self.offset)
        #     yield scrapy.Request(url, callback = self.parse)


        # 第二种写法：直接从response获取需要爬取的连接，并发送请求处理，直到链接全部提取完
        if len(response.xpath("//a[contains(@class,'next')]")) > 0:

            url = response.xpath("//a[contains(@class,'next')]/@href").extract()[0]
            yield scrapy.Request("http:" + url, callback = self.parse)
    #def parse_next(self, response):
    #    pass






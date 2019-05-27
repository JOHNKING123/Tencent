# -*- coding: utf-8 -*-
import scrapy
from Tencent.items import TencentItem, LoLItem


class LoLSpider(scrapy.Spider):
    # 爬虫名
    name = 'tieba'
    # 爬虫爬取数据的域范围
    allowed_domains = ['tieba.baidu.com']
    # 1. 需要拼接的url
    baseURL = "https://tieba.baidu.com/f?kw=%E8%8B%B1%E9%9B%84%E8%81%94%E7%9B%9F&ie=utf-8&pn=750"

    tiebaName = 'lol'
    # 1. 需要拼接的url地址的偏移量
    offset = 0
    # 爬虫启动时，读取的url地址列表
    start_urls = [baseURL + str(offset)]



    # 用来处理response
    def parse(self, response):
        # 提取每个response的数据
        node_list = response.xpath("//ul[@id='thread_list']/li")
        if node_list == None or len(node_list) == 0 :
            return

        for node in node_list:
            print node.attrib['class']
            if 'j_thread_list' in node.attrib['class']:
                # 构建item对象，用来保存数据
                item = LoLItem()
                # 提取每个职位的信息，并且将提取出的Unicode字符串编码为UTF-8编码
                item['replyNum'] = node.xpath("./div/div")[0].xpath("./span/text()").extract()[0].encode("utf-8")

                item['title'] = node.xpath("./div/div")[1].xpath("./div")[0].xpath("./div")[0].xpath("./a/text()").extract()[0].encode("utf-8")

                names = node.xpath("./div/div")[1].xpath("./div")[0].xpath("./div")[1].xpath("./span/span[@class='frs-author-name-wrap']/a/text()").extract();
                if len(names) > 0 :
                    item['authorName'] = node.xpath("./div/div")[1].xpath("./div")[0].xpath("./div")[1].xpath("./span/span[@class='frs-author-name-wrap']/a/text()").extract()[0].encode("utf-8")
                else:
                    item['authorName'] = ''

                createdTimes = node.xpath("./div/div")[1].xpath("./div")[0].xpath("./div")[1].xpath("./span[contains(@class,'is_show_create_time')]/text()").extract();
                if len(createdTimes) > 0 :
                    item['createdTime'] = createdTimes[0].encode("utf-8")
                else:
                    item['createdTime'] = ''
                # yield 的重要性，是返回数据后还能回来接着执行代码
                yield item

        # 第一种写法：拼接url，适用场景：页面没有可以点击的请求连接，必须通过拼接url才能获取响应
        # if self.offset < 2190:
        #     self.offset += 10
        #     url = self.baseURL + str(self.offset)
        #     yield scrapy.Request(url, callback = self.parse)


        # 第二种写法：直接从response获取需要爬取的连接，并发送请求处理，直到链接全部提取完
        if len(response.xpath("//a[contains(@class,'next pagination-item')]")) > 0:

            url = response.xpath("//a[contains(@class,'next pagination-item')]/@href").extract()[0]
            yield scrapy.Request("http:" + url, callback = self.parse)
    #def parse_next(self, response):
    #    pass






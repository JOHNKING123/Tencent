# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TencentItem(scrapy.Item):
    #职位名
    positionName = scrapy.Field()

    #职位详情连接
    positionLink = scrapy.Field()

    #职位类别
    positionType = scrapy.Field()

    #招聘人数
    peopleNumber = scrapy.Field()

    #工作地点
    workLocation = scrapy.Field()

    #发布时间
    publishTime = scrapy.Field()


class LoLItem(scrapy.Item):
    #标题
    title = scrapy.Field()

    #作者名称
    authorName = scrapy.Field()

    #回复数
    replyNum = scrapy.Field()

    #创建时间
    createdTime = scrapy.Field()


class TiebaItem(scrapy.Item):
    #贴吧名称
    tiebaName = scrapy.Field()

    #标题
    title = scrapy.Field()

    #作者名称
    authorName = scrapy.Field()

    #回复数
    replyNum = scrapy.Field()

    #创建时间
    createdTime = scrapy.Field()


class TiebaUrlItem(scrapy.Item):
    #主题
    title = scrapy.Field()

    #名称
    name = scrapy.Field()

    #链接
    url = scrapy.Field()


class   BaUrlItem(scrapy.Item):

    id = scrapy.Field()

    #相对类型
    relativeType = scrapy.Field()

    #链接
    url = scrapy.Field()

    #链接描述
    urlDesc = scrapy.Field()

    #基本地址
    baseUrl = scrapy.Field()

    #使用标记
    usedFlag = scrapy.Field()





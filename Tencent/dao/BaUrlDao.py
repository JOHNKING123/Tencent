# coding=utf-8
import pymysql

from Tencent.items import BaUrlItem

import Queue

class BaUrlDao:
    def __init__(self):
        self.data = []
        self.db = pymysql.connect("47.105.143.13", "root", "123456", "testDb", charset="utf8")

        self.cursor = self.db.cursor()

        self.itemList = []

        self.queue = Queue.Queue()

    def saveItem(self, item):

        checkRs = self.checkExist(item)
        if checkRs:
            return

        sql = "INSERT INTO ba_url(relative_type,url,url_desc,base_url) \
                   VALUES (%s,\'%s\',\'%s\',\'%s\')" % \
              (item['relativeType'],item['url'],item['urlDesc'],item['baseUrl'])
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
            raise

    def checkExist(self,item):

        sql = "select * from ba_url t WHERE t.relative_type = %s and url= \'%s\'" % \
              (item['relativeType'],item['url'])
        try:
            self.cursor.execute(sql)
            rs = self.cursor.fetchall()
            if len(rs) > 0:
                return True
            return False
        except:
            return False

    def dealUsedItem(self,item):

        sql = "update ba_url set used_flag = 1 WHERE id = %s" % \
              (item['id'])

        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
            raise

    def getItems(self):

        sql = "select * from ba_url WHERE used_flag = 0 limit 10000"

        self.cursor.execute(sql)

        rs = self.cursor.fetchall()

        print rs

        items = []
        for record in rs:
            item = BaUrlItem()
            item['id'] = record[0]
            item['relativeType'] = record[4]
            item['url'] = record[5]
            item['urlDesc'] = record[6]
            item['baseUrl'] = record[7]
            item['usedFlag'] = record[8]
            items.append(item)

        return items

    def  getOneItem(self):

        if not self.queue.empty():
            item = self.queue.get()

            return item
        else:
            items = self.getItems()
            for item in items:
                self.queue.put(item)
            if not self.queue.empty():
                return self.queue.get()

    def __del__(self):
        self.db.close()

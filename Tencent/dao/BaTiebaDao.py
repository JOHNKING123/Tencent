# coding=utf-8
import pymysql


class BaTiebaDao:
    def __init__(self):
        self.data = []
        self.db = pymysql.connect("47.105.143.13", "root", "123456", "testDb", charset="utf8")

        self.cursor = self.db.cursor()

    def saveItem(self, item):

        sql = "INSERT INTO ba_tieba(tieba_name,title, \
                   author_name, reply_num) \
                   VALUES (\'%s\', \'%s\',%s)" % \
              (item['tiebaName'],item['title'], item['authorName'], item['replyNum'])
        try:
            # 执行sql语句
            self.cursor.execute(sql)
            # 提交到数据库执行
            self.db.commit()
        except:
            # 如果发生错误则回滚
            self.db.rollback()
            raise

    def __del__(self):
        self.db.close()

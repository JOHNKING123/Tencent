# coding=utf-8
import pymysql

from Tencent.dao.BaPositionDao import BaPositonDao
from Tencent.items import TencentItem

db = pymysql.connect("47.105.143.13", "root", "123456", "testDb",charset="utf8")

cursor = db.cursor()

cursor.execute("SELECT VERSION()")

data = cursor.fetchone()

# 测试注释
print ("Database version : %s " % data)
#
# sql = """INSERT INTO ba_position(position_name,
#          people_number, work_location, position_type, position_link,publish_time)
#          VALUES ('27216-腾讯乘车码-客户端资深开发工程师', 2, '技术类', '深圳', 'position_detail.php?id=47343&keywords=&tid=0&lid=0','2019-01-29')"""
# try:
#    # 执行sql语句
#    cursor.execute(sql)
#    # 提交到数据库执行
#    db.commit()
# except:
#    # 如果发生错误则回滚
#    db.rollback()

item = TencentItem()
item['positionName'] = '27216-腾讯乘车码-客户端资深开发工程师'

item['positionLink'] = 'position_detail.php?id=47343&keywords=&tid=0&lid=0'

item['positionType'] = '技术类'

item['peopleNumber'] = 2

item['workLocation'] = '深圳'

item['publishTime'] = '2019-01-29'
positionDao = BaPositonDao()

positionDao.saveItem(item)



db.close()

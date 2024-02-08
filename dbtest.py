import pymysql
import prettytable as pt
import argparse
import configparser

con_f="config.ini"
conf=configparser.ConfigParser()
conf.read(con_f,encoding='utf-8')
sections=conf.sections()
print(conf.items('aliyun'))
def get_parser():
    parser = argparse.ArgumentParser(description='查询学校近三年专业组投档线')
    parser.add_argument('name', type=str, default='武汉科技大学', help="传入学校校名")
    return parser.parse_args().name

# 连接数据库
db = pymysql.connect(host=conf['aliyun']['host'],
                     user=conf['aliyun']['user'],
                     password=conf['aliyun']['password'],
                     database=conf['aliyun']['database'])
cursor = db.cursor()
cursor.execute("select version()")
data = cursor.fetchone()
print(data)

print(get_parser())
# 创建table表头
table=pt.PrettyTable(['学校代码','学校名称','专业组','层次','组合','投档线','分数分位','年度'])
sql = 'SELECT c_code,c_name,s_code,grade,class,score,(SELECT total FROM gkscore WHERE gkscore.class=collegescore.class AND gkscore.score=collegescore.score AND gkscore.year=collegescore.y) AS location,y FROM collegescore WHERE c_name=%s order BY s_code,y LIMIT 1000;'
print(sql)
try:
    cursor.execute(sql,get_parser())
    results=cursor.fetchall()
    for row in results:
        # 为表添加行数据
        table.add_row([row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7]])
except:
    print("error:can't fetch db")
print(table)
cursor.close()
db.close()

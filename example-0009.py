import pymysql

conn = pymysql.connect(host='localhost', port=3306, user='root', password='root', database='djangoblog', charset='utf8')
cursor = conn.cursor()
sql = 'select * from conf_tc_command'
cursor.execute(sql)
for item in cursor.fetchall():
    print(item)

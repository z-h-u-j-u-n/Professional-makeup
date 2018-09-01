# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pymysql

conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', passwd='ques0132qq', db='cos', charset='utf8')
cursor = conn.cursor()

def select(cursor):
    # 查询
    sql_s = 'select * from Patron'
    cursor.execute(sql_s)
    row_s = cursor.fetchmany(100)
    return row_s

def select_all(cursor):
    print('查询所有记录：')
    for s in select(cursor):
        print(s)
        
def insert(conn, cursor):
    # 增加
    cursor.execute("insert into Patron(patron_id, name, address) \
           values(%s, %s, %s)", ['568', '许晴亮', '文荟公寓'])
    conn.commit()
    select_all(cursor)

def delete(conn, cursor):
    # 删除
    cursor.execute("delete from Patron where patron_id like %s", ['568'])
    conn.commit()
    select_all(cursor)

def update(conn, cursor):
    # 更新
    cursor.execute("update Patron set name = %s where patron_id like %s", ['xql', '568'])
    conn.commit()
    select_all(cursor)
        
print('增加一条记录...')
insert(conn, cursor)

print('修改记录:')
update(conn, cursor)

print('删除记录：')
delete(conn, cursor)


cursor.close()
conn.close()



    


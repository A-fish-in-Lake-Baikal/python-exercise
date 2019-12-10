# coding=utf-8
'''
author:马维畅
time：2019/5/10 14:42
'''

import pymssql
def sqlexecute():
    conn = pymssql.connect('192.168.2.185','sa','test12#$%','PSUM9')
    cursor = conn.cursor()

    sql = """SELECT *  FROM [PSUM9].[dbo].[CC_SYSTEM_USER]"""

    cursor.execute(sql)
    for row in cursor:
        print(row)
    conn.commit()
    conn.close()

if __name__=='__main__':
        sqlexecute()

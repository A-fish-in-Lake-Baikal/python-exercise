import configparser
import pymssql
import socket


class SQLServer(object):
    def __init__(self,host,user,password,database,charset):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.charset = charset

    def GetConnect(self):
        if not self.database:
            raise(NameError,"NO DataBase")
        self.conn = pymssql.connect(host=self.host,user=self.user,password=self.password,database=self.database,charset=self.charset)
        cursor =  self.conn.cursor()
        if not cursor:
            raise(NameError,"Connect faild")
        else:
            print("connect successful")
            return cursor

    def ExecQuery(self,sql):
        cursor = self.GetConnect()
        cursor.execute(sql)
        row = cursor.fetchone()
        count = {}
        for row in cursor:
            name = row[1]
            count[name] = count.get(name,0) +1
        return count
        self.conn.close()

if __name__ == '__main__':
    SQL = SQLServer(host='192.168.1.61',user='sa',password='test12#$%',database='PSUM9',charset='utf8')
    count = SQL.ExecQuery(sql='SELECT *  FROM [PSUM9].[dbo].[Para_Department]')
    items = list(count.items())
    items.sort(key=lambda x:x[1],reverse=True)
    # for i in range(10):
    #     name,number = items[i]
    #     print("{:<10}{:>10}".format(name,number))
    for i in range(len(items)):
        name,number = items[i]
        if number>1:
            print("{:<20}{:>10}".format(name,number))

import configparser
import pymssql
import socket




# hostname = socket.gethostname()
# # print(hostname)
# count = {}
#
# conn = pymssql.connect(host=hostname,user="sa",password="MT19960318",database="PSUM9",charset="utf8")
# cursor = conn.cursor()
#
#
# cursor.execute('SELECT *  FROM [PSUM9].[dbo].[Para_Department]')
# row = cursor.fetchone()
# for row in cursor:
#     # print("{}{}{}{}{}".format(row[1],row[2],row[3],row[4],row[5]))
#     name = row[1]
#     # print(name)
#     count[name] = count.get("name",0) +1
#     # print(count)
#     # print("{}".format(row[1]))
#
# items = list(count.items())
# items.sort(key=lambda x:x[1],reverse=True)
# for i in range(10):
#     name,number = items[i]
#     print("{:<10}{:>10}".format(name,number))
#
# conn.close()


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
    SQL = SQLServer(host='192.168.11.155',user='sa',password='MT19960318',database='PSUM9',charset='utf8')
    count = SQL.ExecQuery(sql='SELECT *  FROM [PSUM9].[dbo].[Para_UserInfo]')
    items = list(count.items())
    items.sort(key=lambda x:x[1],reverse=True)
    # for i in range(10):
    #     name,number = items[i]
    #     print("{:<10}{:>10}".format(name,number))
    for i in range(len(items)):
        name,number = items[i]
        if number>1:
            print("{:<10}{:>10}".format(name,number))

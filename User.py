#後台 可更改服務內容
#連線DB
from re import T
from dbConfig import conn, cur
def getList():
    #查詢
    sql="select id, username,msg, account_number,password from User order by id desc;"
    cur.execute(sql)
    records = cur.fetchall()
    return records

    #`id`, `username`, `account_number`, `password`
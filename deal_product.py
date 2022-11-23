#!C:\Users\何晏禎\AppData\Local\Programs\Python\Python310\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import shopping_cart as gb

'''''
#連線DB
from dbConfig import conn, cur
#先印出http 表頭
'''''
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>移除商品</title>
</head>
<body>
""")

#查詢
form = cgi.FieldStorage()
id=form.getvalue('name')
gb.deal_product(id)

'''''
sql="delete from guestbook where id=%s;"
cur.execute(sql,(id,))
conn.commit()
'''''

if gb.deal_product(id):
    print(f"{id}號商品已刪除!")
else:
    print("delet failed")
print("<br><a href='clothing.py'>返回商品列表</a>")
print("</body></html>")





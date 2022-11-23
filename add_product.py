#!C:\Users\何晏禎\AppData\Local\Programs\Python\Python310\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import shopping_cart as gb

#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>新增產品</title>
</head>
<body>
""")

#查詢
form = cgi.FieldStorage()
product = form.getvalue('name')
cost = form.getvalue('money')
inventory = form.getvalue('num')

"""sql="insert into guestbook (title,msg,nickname) values (%s,%s,%s);"
cur.execute(sql,(title,msg,nick))
conn.commit()"""
if gb.add_product(product,cost,inventory):
    print("商品已存入!")
else:
    print("add failed!")

print("<br><a href='clothing.py'>返回商品列表</a>")
print("</body></html>")

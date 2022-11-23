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
<title>加入購物車</title>
</head>
<body>
""")

#查詢
form = cgi.FieldStorage()
product_id=form.getvalue('i')
num=form.getvalue('j')

goodsList = gb.getList()
gb.add_in_cart(product_id,num)


### 還沒成功

# for (id,product, cost, inventory) in goodsList:
#     if id == product_id:
#         print(f"<p>編號{id}: 商品:{product} 價格:{cost} 庫存:{inventory}</p>")


# print("<br><a href='clothing.py'>返回商品列表</a>")
# print("</body></html>")

if gb.add_in_cart(product_id,num):

    print(f"{product_id}號商品已加入購物車!")
else:
    print("加入失敗")
print("<br><a href='clothing.py'>返回商品列表</a>")
print("</body></html>")





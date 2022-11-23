#!C:\Users\何晏禎\AppData\Local\Programs\Python\Python310\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import shopping_cart as gb

#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
sys.stdout.flush()

#不好的做法
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Guestbook: ListMsg</title>
</head>
<body>
<a href="clothing.py">返回購物頁面</a> <br>
<br> <hr> <br>
購物車列表 
<body>
""")

cartList=gb.get_cart_List()

for (id,product, cost, amount) in cartList:
	print(f"<p>編號{id}: 商品:{product} 價格:{cost} 數量:{amount}</p>")

print("</body></html>")

print("""<br> <hr> <br><a href="change_cart_product.html">更改購物車中的商品</a><br>""")
print("""<a href="change_cart_product.html">結帳</a>  還沒完成""")

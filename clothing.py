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

# goodsList=gb.getList()
# msg=""
# for (id,product, cost, inventory) in goodsList:#msgList->records
# 	msg += f"<p>編號{id}: 商品:{product} 價格:{cost} 庫存:{inventory} </p>"

# with open("clothing.html",'rb') as fp:
#     st=fp.read()
#     st=st.replace(b"###msg###",msg.encode())
#     sys.stdout.buffer.write(st)
# sys.stdout.flush()




#不好的做法
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Guestbook: ListMsg</title>
</head>
<body>
<a href="00.basic html.html">返回首頁</a> <br>
<p> </p>
商品列表 
<a href='add_product_Form.html'> 商品管理   <a href='my_cart.py'>我的購物車 </a><hr>
<form method="post" action="add_in_cart.py">
輸入要加入購物車的商品編號和數量: <input type='text' name='i'><input type='text' name='j'><input type='submit'>  改壞了

</form>
 <hr>
""")
# <input type='text' name='j'>
#輸入要加入購物車的商品數量: <input type='text' name='j'><input type='submit'>
goodsList=gb.getList()
i=0

for (id,product, cost, inventory) in goodsList:#msgList->records
	print(f"<p>編號{id}: 商品:{product} 價格:{cost} 庫存:{inventory}</p>")

print("</body></html>")


# id`, `product`, `cost`, `inventory
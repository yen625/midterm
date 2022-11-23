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
<title>Creat New Account</title>
</head>
<body>
""")


#查詢

form = cgi.FieldStorage()
username=form.getvalue('name')
account_number=form.getvalue('account')
password=form.getvalue('password')

##  `id`, `username`, `account_number`, `password`



if gb.creat_user(username,account_number,password):
    print("帳號創建成功!")
else:
    print("creat failed")

print("<br><a href='loginFrom.html'>回登入頁面</a>")
print("</body></html>")


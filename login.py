#!C:\Users\何晏禎\AppData\Local\Programs\Python\Python310\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import shopping_cart as gb

print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>範例1</title>
</head>
<body>
""")

#查詢
form = cgi.FieldStorage()
number = form.getvalue('user_account')
userpassword = form.getvalue('user_password')
gb.login(number,userpassword)

'''''
sql="delete from guestbook where id=%s;"
cur.execute(sql,(id,))
conn.commit()
'''''

if gb.login(number,userpassword):
    print(f"登入成功!")
else:
    print("登入失敗")

print("<br><a href='00.basic html.html'>回首頁</a>")
print("</body></html>")





#!C:\Users\何晏禎\AppData\Local\Programs\Python\Python310\python.exe
from dbConfig import conn, cur

def getList():
    #查詢
    sql = "select id, product, cost, inventory from shopping_cart order by cost desc limit 3;"
    cur.execute(sql)
    records = cur.fetchall()
    return records

def get_cart_List():
    #查詢
    sql="select id, product, cost, amount from cart_list where id>0;"
    cur.execute(sql)
    records = cur.fetchall()
    return records

# def get_user_List():
#     #查詢
#     sql="select username from User where id>=0;"
#     cur.execute(sql)
#     records = cur.fetchall()
#     return records


def add_product(product_name,cost,inventory):
    sql="insert into shopping_cart (product,cost,inventory) values (%s,%s,%s);"
    cur.execute(sql,(product_name,cost,inventory))
    conn.commit()
    return True

def deal_product(id):
    #查詢
    sql="delete from shopping_cart where id=%s;"   
    cur.execute(sql,(id,))   
    conn.commit()
    return True

def deal_cart_product(id):
    #查詢
    sql="delete from cart_list where id=%s;"   
    cur.execute(sql,(id,))   
    conn.commit()
    return True

def creat_user(username,account_number,password):
    sql="insert into User (username,account_number,password) values (%s,%s,%s);"
    cur.execute(sql,(username,account_number,password))
    conn.commit()
    return True



# def changeproduct(amount, id):
#     if(amount == None):
#         return
#     elif(amount == '0'):
#         sql = "DELETE FROM `product` WHERE `product`.`id` = %s;"
#         cur.execute(sql,(id,))
#         conn.commit()
#     else:
#         sql = "update product set Stock=%s where id=%s;"
#         cur.execute(sql,(amount, id))
#         conn.commit()
#     return True

### 還沒成功

def login(number,userpassword):
    sql="select username from User where account_number = number and password = user_password"
    cur.execute(sql,(number,userpassword))
    conn.commit()
    return True

def add_in_cart(product_id,num):   ### 還沒成功
    
    #sql ="select product_id,product,cost,inventory from shopping_cart where id>0;"
    sql="insert into cart_list (id) values (%s);"
    cur.execute(sql,(product_id,))
    # cur.execute(sql,(product_id,num))
    conn.commit()
    return True

def change_product_information(product_id,product_name,product_cost,product_inventory):   ### 還沒成功
    # if product_name == 'NULL':
    #     product_name = "select product_id,product from shopping_cart where inventory>0;"
    # elif product_cost == 'NULL':
    #     product_cost = "select product_id,cost from shopping_cart where inventory>0;"
    # elif product_inventory == 'NULL':
    #     product_inventory = "select product_id,inventory from shopping_cart where inventory>0;"

    sql="update shopping_cart set product=product_name,cost=product_cost, inventory=product_inventory where id = product_id"
    cur.execute(sql)
    conn.commit()
    return True






# product_id`, `product`, `cost`, `inventory
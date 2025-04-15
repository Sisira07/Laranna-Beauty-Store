import mysql.connector as sqltor

def create_table():
    conn=sqltor.connect(host='localhost', user='root', passwd='sisira@dl07', database='ingredients')
    cursor=conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            Product_Name VARCHAR(50),
            Quantity INTEGER,
            Price INTEGER )''')
    conn.commit()
    conn.close()

def insert_product(p_name, quantity, price):
    conn=sqltor.connect(host='localhost', user='root', passwd='sisira@dl07', database='ingredients')
    cursor=conn.cursor()
    Q1='INSERT INTO Products(Product_Name, Quantity, Price) VALUES(%s,%s,%s)'
    V1=(p_name, quantity, price)
    cursor.execute(Q1, V1)
    conn.commit()
    conn.close()
    
def delete_product():
    conn=sqltor.connect(host='localhost', user='root', passwd='sisira@dl07', database='ingredients')
    cursor=conn.cursor()
    cursor.execute('DELETE FROM Products')
    conn.commit()
    conn.close()

'''def update_product(r_id, new_name, new_stock, new_cost, new_status, new_comment='-'):
    conn=sqltor.connect(host='localhost', user='root', passwd='password', database='farm')
    cursor=conn.cursor()
    Q3='UPDATE Resources SET Resource_Name= %s, Quantity_in_stock=%s, Purchase_Cost=%s, Current_Status =%s, Comments=%s WHERE Resouce_ID=%s'
    V3=(new_name, new_stock, new_cost, new_status, new_comment, r_id)
    cursor.execute(Q3, V3)
    conn.commit()
    conn.close()'''
create_table()

def count_p():
    conn=sqltor.connect(host='localhost', user='root', passwd='sisira@dl07', database='ingredients')
    cursor=conn.cursor()
    cursor.execute('SELECT SUM(Price) FROM PRODUCTS')
    count= cursor.fetchall()
    conn.close()
    return count


create_table()

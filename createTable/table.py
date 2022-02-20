import mysql.connector

db= mysql.connector.connect(host= 'localhost', user='root', password='123456', database='mydb')

cur= db.cursor()

cur.execute("CREATE TABLE customers (name VARCHAR(200))")


import mysql.connector

mydb= mysql.connector.connect(host="localhost", user="root", password="123456")

cur= mydb.cursor()

cur.execute("SHOW DATABASES")

for x in cur:
    print(x)

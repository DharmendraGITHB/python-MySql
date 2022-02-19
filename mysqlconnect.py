import mysql.connector as connector


con= connector.connect(host='localhost',
        port ='3306', 
        user='root',
        password='123456',
        database='pythontest')

print(con)

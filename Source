import mysql.connector

name = str(input("insert name!!!"))
age = int(input("insert age!!!"))
gender = str(input("insert sex!"))
mydb = mysql.connector.connect(host="your host name",user="your username",password="*******",database='your database name')
cursor = mydb.cursor()
cursor.execute(cursor.execute('INSERT INTO */your table name/* VALUES (\'%s\',\'%i\',\'%s\')' % (name , age , gender)))
mydb.commit()
cursor.close()
mydb.close() 
print(mydb)

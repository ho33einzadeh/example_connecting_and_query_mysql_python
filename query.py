#QUERY
import mysql.connector

mydb = mysql.connector.connect(host="your host name",user="your user name",password="*******",database='your data base name')
cursor = mydb.cursor()
query = 'SELECT * FROM people;'
cursor.execute(query)
for (name , sex ,age) in cursor:
  print("{},{},{}".format(name,sex,age))

cursor.close()
mydb.close() 

# example_connecting_mysql_python
An example of Connecting a MySQL Database with Python Code

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
This project is simple Lorem ipsum dolor generator.
	
## Technologies
Project is created with:
* Lorem version: 12.3
* Ipsum version: 2.33
* Ament library version: 999
	
## Setup
* To run this project,You must first Step install the Python connector and the mysql database on the system:
in Cmd(Windows Command Line)(os = windows) or Terminal(os= MacOs)
* In the second Step, we write a series of Python code related to the database connection in the IDE


### in Windows Command Line(CMD):
```diff
@@ pip install mysql-connector-python @@
```
#### Important note:
Note that if you do not write the word 'Python' at the end of the command, you will encounter this error:

* mysql.connector.errors.NotSupportedError: Authentication plugin 'caching_sha2_password' is not supported
### in Terminal MacOs:
```diff
@@ sudo apt-get install mysql-connector-python @@
```
### After:
```diff
<!--- @@ --->  pip install mysql-connector-python <!--- @@ ---> 

```
#### Now we go to the Python code section in the corresponding IDE( Like vscode:)))) ):
```diff
+ #import my SQL/Python Connector on CodeSpace
import mysql.connector
+ #Send and Pour Information Database With one variable
mydb = mysql.connector.connect(host="your host name",user="your user name",password="your pass",database='your database name')

+ #Create Cursor on Cmd Structure
cursor = mydb.cursor()
+ #Execute MySQL Code On CMD space
cursor.execute(cursor.execute('INSERT INTO people VALUES ("YOUR VALUEWS)')
+ #do 
mydb.commit()
cursor.close()
mydb.close() 
print(mydb)
```




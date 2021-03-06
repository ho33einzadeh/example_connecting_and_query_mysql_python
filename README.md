
# An example of Connecting And Query Data a MySQL Database with Python Code And How to install

![](https://s21.picofile.com/file/8444189792/Untitled_1.png)

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
In this project, we will examine how to connect a database  and Query data with Python code in windows and macOS operating systems
	
## Technologies
Project is created with:
* Python version: 3.10.0
* pip version: 21.3.1
* Mysql Connector python Version for win64: > https://bit.ly/3HJg57l
	
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
@@ pip install mysql-connector-python @@

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


#### Important note:
##### Note that Python must be installed on your system + Python pip must also + python and SQL connector Be installed

## A series of MYSQL code commands:
##### SELECT - extracts data from a database
##### UPDATE - updates data in a database
##### DELETE - deletes data from a database
##### INSERT INTO - inserts new data into a database
##### CREATE DATABASE - creates a new database
##### ALTER DATABASE - modifies a database
##### CREATE TABLE - creates a new table
##### ALTER TABLE - modifies a table
##### DROP TABLE - deletes a table
##### CREATE INDEX - creates an index (search key)
##### DROP INDEX - deletes an index

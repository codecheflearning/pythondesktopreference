import sqlite3 as driver

def get_connection():
    con = driver.connect("pyquickref.db")
    print("new connection created")
    return con


connection = get_connection()
handle = connection.cursor()
#Drop table if already exists. Uncomment this line when running second time
handle.execute("drop table book")
#Create a table
handle.execute("create table book(name, publisher, author, publish_date, type)")
#insert some data. Insert statement implictly opens a transaction
handle.execute("insert into book(name, publisher, author, publish_date, type) "
               "values ('Python Quick Ref', 'Amazon', 'Govind', '12-10-2024', 'paperback')")
#commit transaction
connection.commit()
#read data from table now
result = handle.execute("select * from book")

for row in result:
    print(row)

#Close handle
handle.close()
#Close connection
connection.close()



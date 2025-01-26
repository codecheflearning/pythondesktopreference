#dbm is a key value store in memory database similar to dictionary
import dbm

# mode 'c' created a new db for reading and writing.
# #It creates a new one if it does not exist.
def get_connection(dbname):
    return dbm.open(dbname,'c')

#Create connection
connection = get_connection("book.db")

#insert key value pairs
connection['name'] = 'Python Quick Ref'
connection['publisher'] = 'amazon'
connection['publish_date'] = '10/02/2024'
connection['type'] = 'ebook'
connection['subject'] = 'Coding in Python'

#read rows
for row in connection.values():
	print(row)

#Or read using key value
for key, value in connection.items():
	print(key, value)

# closing the connection.
connection.close()


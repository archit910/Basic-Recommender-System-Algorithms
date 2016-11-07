import sqlite3

conn = sqlite3.connect('Products.db')

print "Database Connected"

conn.execute('''CREATE TABLE PRODUCT
			(ID INT PRIMARY KEY NOT NULL,
			NAME TEXT NOT NULL,
			TAGS TEXT NOT NULL);''')

print "Table Created SUCCESSFULLY"
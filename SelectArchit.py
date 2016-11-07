import sqlite3
conn = sqlite3.connect('user.db')

cursor = conn.execute("SELECT NAME from USERS")
for row in cursor:
	print "name is " , row[0]
print "Operation Done Successfully"
conn.close();

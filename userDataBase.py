import sqlite3
conn = sqlite3.connect('user.db')
print 'DataBase Connected'

conn.execute('''CREATE TABLE USERS 
		(ID INT PRIMARY KEY NOT NULL,
		NAME  TEXT NOT NULL,
		PASSWORD TEXT NOT NULL);''')
print "Table Created Succesfully";
				
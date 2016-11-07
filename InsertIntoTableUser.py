import sqlite3

conn = sqlite3.connect('user.db')

print "Opened Database Succesfully"
 # DO NOT RUN IT  
 # 1234 is the default password for all dummy users
conn.execute("INSERT INTO USERS (ID,NAME,PASSWORD)  VALUES (1 , 'Archit' ,'1234')")
conn.execute("INSERT INTO USERS (ID,NAME,PASSWORD)  VALUES (2 , 'Shivam' ,'1234')")
conn.execute("INSERT INTO USERS (ID,NAME,PASSWORD)  VALUES (3 , 'Shruti' ,'1234')")
conn.execute("INSERT INTO USERS (ID,NAME,PASSWORD)  VALUES (4 , 'Tanmay' ,'1234')")
conn.execute("INSERT INTO USERS (ID,NAME,PASSWORD)  VALUES (5 , 'Rishabh' ,'1234')")
conn.execute("INSERT INTO USERS (ID,NAME,PASSWORD)  VALUES (6 , 'Manvi' ,'1234')")
conn.execute("INSERT INTO USERS (ID,NAME,PASSWORD)  VALUES (7 , 'Ayushman' ,'1234')")
conn.execute("INSERT INTO USERS (ID,NAME,PASSWORD)  VALUES (8 , 'Satyam' ,'1234')")
conn.execute("INSERT INTO USERS (ID,NAME,PASSWORD)  VALUES (9 , 'Yash' ,'1234')")
conn.execute("INSERT INTO USERS (ID,NAME,PASSWORD)  VALUES (10 , 'Neha' ,'1234')")


conn.commit()
print "Archit saved"
conn.close()
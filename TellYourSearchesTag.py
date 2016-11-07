import sqlite3




if __name__ == '__main__':
	check = False

	user_name = str(raw_input("Enter The User Name "))

	passkey = str(raw_input("Enter The Password "))

	conn = sqlite3.connect('user.db')

	conn2 = sqlite3.connect('Products.db')

	cursor = conn.execute("SELECT NAME , PASSWORD from USERS")
	 
	for row in cursor:
		if(row[0] == user_name and row[1] == passkey):
			print "USER VERIFIED"
			check = True
			break
	if(check == False):

		print "WRONG USERNAME/PASSWORD"
		exit(0)



	print "Search the item in my products : - "
	My_search = str(raw_input().split(' '))

	cursor2 = conn2.execute("SELECT tags , name from PRODUCT")
	for row in cursor2:
		TAGG = str(row[0]).split('+')
		for each in TAGG:
			if(each in My_search):
				print "Recommend This Product :- *",row[1],"*" 
		


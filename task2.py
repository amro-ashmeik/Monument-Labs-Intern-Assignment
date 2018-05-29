import mysql.connector
from intercom.client import Client

intercom = Client(personal_access_token='my_personal_access_token')

try:
	cnx = mysql.connector.connect(user='user', password='password',
	                              host='127.0.0.1',
	                              database='users')
except mysql.connector.Error as err:
	if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
		print("Incorrect username or password")
	elif err.errno == errorcode.ER_BAD_DB_ERROR:
		print("Database does not exist")
	else:
		print(err)

cursor = cnx.cursor()
query = ("SELECT * FROM user")
cursor.execute(query)

#'id' is a built-in Python function so in application, this would not work. A work-around such as re-naming the 'id' column is necessary.
for (id, name, email) in cursor:
	user = intercom.users.create(email=email, name=name, id=id)

cursor.close()
cnx.close()

try:
	print(gi)
except mysql.error as err:
	print(what)


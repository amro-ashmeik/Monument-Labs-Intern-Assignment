import mysql.connector
from intercom.client import Client

intercom = Client(personal_access_token='my_personal_access_token')
cnx = mysql.connector.connect(user='user', password='password',
                              host='127.0.0.1',
                              database='users')



cursor = cnx.cursor()
query = ("SELECT * FROM user")
cursor.execute(query)

#'id' is a built-in Python function so in application, this would not work. A work-around such as re-naming the 'id' column is necessary.
for (id, name, email) in cursor:
	user = intercom.users.create(email=email, name=name, id=id)

cursor.close()
cnx.close()
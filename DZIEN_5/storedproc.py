#example 1

import mysql.connector

# create a connection to the MySQL server
cnx = mysql.connector.connect(user='<username>', password='<password>',
                              host='<hostname>', database='<database_name>')

# create a cursor
cursor = cnx.cursor()

# call the stored procedure
cursor.callproc('your_stored_procedure_name', args)

# fetch results, if any
for result in cursor.stored_results():
    print(result.fetchall())

# close cursor and connection
cursor.close()
cnx.close()

#example 2

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# establish a connection to the MySQL server
engine = create_engine("mysql+mysqlconnector://<username>:<password>@<hostname>/<database_name>")

# create a session for the transaction
Session = sessionmaker(bind=engine)
session = Session()

# call the stored procedure
result_proxy = session.execute("CALL your_stored_procedure_name(:arg)", {'arg': args})

# fetch results, if any
results = result_proxy.fetchall()
for result in results:
    print(result)

# close the session
session.close()

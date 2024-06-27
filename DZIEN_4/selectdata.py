import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',port='3306',database='pierwszabaza')

cursorObject = db.cursor()

query = 'SELECT studentnb,firstname,lastname FROM student'
cursorObject.execute(query)

result = cursorObject.fetchall()
print(type(result))

for x,y,z in result:
    print(f'student nr {x}, {y} {z}')

print('_'*50)

viewquery = 'SELECT * FROM indeksy'
cursorObject.execute(viewquery)
result = cursorObject.fetchall()

for x,y in result:
    print(f'student: {x} {y}')

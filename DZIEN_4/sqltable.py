import mysql.connector

db = mysql.connector.connect(user='root',password='abc123',host='127.0.0.1',port='3306',database='pierwszabaza')

cursorObject = db.cursor()
tabela_student = """
CREATE TABLE IF NOT EXISTS student(
firstname varchar(100),
lastname varchar(100),
studentnb int primary key);
"""
cursorObject.execute(tabela_student)

dodaj_studenta = "INSERT INTO student(firstname, lastname, studentnb) values(%s,%s,%s);"
val_one = ("Jan","Kot",3123123)

cursorObject.execute(dodaj_studenta,val_one)

val_multi = [
    ("Maria","Wasek",844335),
    ("Marek","Neptus",342355),
    ("Leon","Rok",534554),
    ("Nadia","Kos",84435),
    ("Romek","Tym",846126),
    ("Henio","Rym",84123),
    ("Marta","Woś",85676)
]
cursorObject.executemany(dodaj_studenta,val_multi)
db.commit()
db.close()

import sqlalchemy
import mysql.connector

from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker


engine = sqlalchemy.create_engine('mysql+mysqlconnector://root:abc123@localhost:3306/pierwszabaza',echo=True)
class Base(DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer,primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.String(length=50))
    fullname = sqlalchemy.Column(sqlalchemy.String(length=50))
    nickname = sqlalchemy.Column(sqlalchemy.String(length=50))

    def __repr__(self):
        return f'<User -> name: {self.name}, fullname: {self.fullname}, nickname: {self.nickname}>'

Base.metadata.create_all(engine)

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

us1 = User(name='Marcin',fullname='Marcin Albiniak',nickname='albin')
session.add(us1)

us2 = User(name='Ewa',fullname='Ewa Kot',nickname='kotek')
session.add(us2)

us3 = User(name='Olaf',fullname='Olaf Knot',nickname='oli')
session.add(us3)

us4 = User(name='Marcin',fullname='Marcin Nowak',nickname='nomo')
session.add(us4)

#wiele rekordów

usrs = [
User(name='Olo',fullname='Olo Franz',nickname='ol'),
User(name='Jaga',fullname='Jaga Franz',nickname='jg'),
User(name='Roma',fullname='Roma Franz',nickname='rm')
]

session.add_all(usrs)

session.commit()

print("_"*50)
for s in session.query(User).all():
    print(s)

print("_"*50)
for s in session.query(User).filter(User.name == "Marcin"):
    print(s.fullname)

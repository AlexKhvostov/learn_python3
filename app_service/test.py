from builtins import print

import sqlalchemy #начните работу с этой библиотеки
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper, sessionmaker

engine = create_engine("mysql://alex:123@localhost/Learn?host=localhost?port=3306")
Session = sessionmaker(bind=engine)
session = Session()

conn = engine.connect()
conn.execute("SELECT * FROM dept")

print("Версия SQLAlchemy:", sqlalchemy.__version__)  # посмотреть версию SQLALchemy

metadata = MetaData()
users_table = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(30)),
    Column('fullname', String(30)),
    Column('password', String(30))
)
metadata.create_all(engine)

class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)

mapper(User, users_table)
# <Mapper at 0x...; User>


# Вывод параметров на экран для контроля и понимания.
#print(mapper(User, users_table))

user = User("Вася", "Василий", "qweasdzxc")
vasiaUser = User("vasia", "Vasiliy Pypkin", "vasia2000")
session.add(vasiaUser)

session.add_all([User("kolia", "Cool Kolian[S.A.]","kolia$$$"), User("zina", "Zina Korzina", "zk18")])
vasiaUser.password = "-=VP2001=-"

ourUser = session.query(User).filter_by(name="vasia").first()


#Сессия внимательно следит за нами. Она, для примера, знает, что Вася был модифицирован:
print("--")
print("session.dirty", session.dirty)
print("--")
#И что еще пара User’ов ожидают сброса в базу:
print("--")
print("session.new",session.new)
print("--")

#Занесения изменений в базу
#session.commit()

print("vasiaUser: ",vasiaUser)
print("vasiaUser.id: ",vasiaUser.id)
print("engine: ", engine)
print("metadata: ", metadata)
print("Session: ", Session)
print("session: ", session)
print("ourUser: ",ourUser)

print("vasiaUser.id: ",vasiaUser.id)

print("Вывод данных из таблицы по запросу: ")

k=0
for id, name, fullname in session.query(User.id, User.name, User.fullname):
    print (k+1, id, name, fullname)
    k=k+1
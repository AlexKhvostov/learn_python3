import sqlalchemy #начните работу с этой библиотеки
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper

engine = create_engine(
      "mysql://alex:123@localhost/Learn?host=localhost?port=3306")

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


#print(mapper(User, users_table))
user = User("Вася", "Василий", "qweasdzxc")
print(user)
print(user.id)
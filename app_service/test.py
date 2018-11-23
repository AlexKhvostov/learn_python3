from builtins import print

import sqlalchemy #начните работу с этой библиотеки
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper, sessionmaker

#Создаем подключение к базе данных с использованием логина и пароля
engine = create_engine("mysql://alex:123@localhost/Learn?host=localhost?port=3306")
#открываем сессию  ( пока не понятно замем. В расках сессии идет работа с базой и пользователями.
Session = sessionmaker(bind=engine)
# Создаем объекат session класса Session() для общения с базой данных
session = Session()

# тестовые запросы к базе
#conn = engine.connect()
#conn.execute("SELECT * FROM dept")

#тестирование состояния модуля.
#print("Версия SQLAlchemy:", sqlalchemy.__version__)  # посмотреть версию SQLALchemy


''' привязываем таблицы к коду'''
metadata = MetaData()
''' таблица пользователей '''
users_table = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(30)),
    Column('fullname', String(30)),
    Column('password', String(30))
)
''' таблица отделов '''
dept_table = Table('dept', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50))
)

'''создаем описаные таблица , в метод встроена проверка наличия таких баз'''
metadata.create_all(engine)

'''Создаем классы для работы с таблицами в коде python'''
''' User'''
class User(object):
    def __init__(self, name, fullname, password):
        self.name = name
        self.fullname = fullname
        self.password = password

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name, self.fullname, self.password)

''' Dept'''
class Dept(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Dept('%s')>" % (self.name)


'''метода для слияния таблицы и класса '''
mapper(User, users_table)
mapper(Dept, dept_table)
# <Mapper at 0x...; User>

''' создаем и проверяем объект типа :'''
#User
t_user = User("vasia", "Vasilij", "qweasdzxc")
#Dept
t_dept = Dept("developer")

#vasiaUser = User("vasia", "Vasiliy Pypkin", "vasia2000")
#session.add(vasiaUser)

''' создание и добавление в сессию объектов классов  User и Dept'''
session.add(t_user) # добавление одной записи ( объектов )
session.add(t_dept) # --//--//--
session.add_all([Dept("cleaner"), Dept("logists")]) # добваление множества записей (объектов )
session.add_all([User("kolia", "Cool Kolian[S.A.]","kolia$$$"), User("zina", "Zina Korzina", "zk18")]) # --//--
#t_user.password = "-=VP2001=-"

''' объект запроса '''
#ourUser = session.query(User).filter_by(name="Вася").first()

oneOfDept = session.query(Dept)

print("oneOfDept: ",oneOfDept)



#Сессия внимательно следит за нами. Она, для примера, знает, что Вася был модифицирован:
print("--")
print("session.dirty: ", session.dirty)
print("--")
#И что еще пара User’ов ожидают сброса в базу:
print("--")
print("session.new: ",session.new)
print("--")


#Занесения изменений в базу
session.commit()

#print("vasiaUser: ",vasiaUser)
#print("vasiaUser.id: ",vasiaUser.id)
print("engine: ", engine)
print("metadata: ", metadata)
print("Session: ", Session)
print("session: ", session)
#print("ourUser: ",ourUser)


print("Вывод данных из таблицы по запросу: ")

k=0
for id, name, fullname in session.query(User.id, User.name, User.fullname):
    print (k+1, id, name, fullname)
    k=k+1

'''
for name in session.query(.id, User.name, User.fullname):
    print (k+1, id, name, fullname)
    k=k+1
'''
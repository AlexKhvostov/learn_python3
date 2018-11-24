from builtins import print

import sqlalchemy #начните работу с этой библиотеки
from datetime import date
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper, sessionmaker


#Создаем подключение к базе данных с использованием логина и пароля
engine = create_engine("mysql://alex:Protokol911#@localhost/Learn?host=localhost?port=3306")
#открываем сессию  ( пока не понятно замем. В расках сессии идет работа с базой и пользователями.
Session = sessionmaker(bind=engine)
# Создаем объекат session класса Session() для общения с базой данных
session = Session()

1
''' привязываем таблицы к коду'''
metadata = MetaData()
''' таблица отделов '''
dept_table = Table('dept', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(50))
)

''' таблица работников '''
workers_table = Table('workers', metadata,
    Column('id', Integer, primary_key=True),
    Column('deptname', String(30)),
    Column('fullname', String(30)),
    Column('birthday', String(30)), # в будущем поменять на дату
    Column('salary', Integer)
)
'''создаем описаные таблица , в метод встроена проверка наличия таких баз'''
metadata.create_all(engine)


''' создаем объекты класса Dept'''
class Dept(object):
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Dept('%s')>" % (self.name)

''' создаем объекты класса Workers'''
class Workers(object):
    def __init__(self, deptname, fullname, birthday, salary):
        self.deptname = deptname
        self.fullname = fullname
        self.birthday = birthday
        self.salary = salary

    def __repr__(self):
        return "<Workers('%s','%s', '%s', '%s')>" % (self.deptname, self.fullname, self.birthday, self.salary)

'''метода для слияния таблицы и класса '''
mapper(Dept, dept_table)
mapper(Workers, workers_table)




def selectBases():
    sBase = 0
    while (sBase != 1) and (sBase != 2):
        sBase = int(input("----------------------------------\n"
                          "| Выберите базу данных для работы: \n"
                          "| 1 - отделы.  \n"
                          "| 2 - сотрудники \n"
                          "| Ваш выбор : "))
    return(sBase)


def selectAct():
    nAct=0
    while (nAct != 1) and (nAct != 2) and (nAct != 3):
        nAct = int(input("----------------------------------\n"
                         "| Выберите действие для обработки: \n"
                          "| 1 - добавить запись.  \n"
                          "| 2 - удалить запись \n"
                          "| 3 - просмотреть записи \n"
                          "| Ваш выбор : "))
    return(nAct)

def useBases(n):
    pass

def addItem(base):
    if base == 1:
        print("-------------\n Добавляем запись в таблицу 'отделы'.")
        deptname=input("Введите название отдела:")
        item = Dept(deptname)
    elif base == 2:
        print("-------------\n Добавляем запись в таблицу 'сотрудники'.")
        deptname = int(input("Выберите название отдела(число до 10): ")) # должны дергаться из базы . решить перебором через if.
        fullname = input("Введите имя сотрудника: ")
        birthday = input("Введите дату рождения: ")
        salary = int(input("Ввдите зарплату сотрудника: "))
        item = Workers(deptname, fullname, birthday, salary)
    else:
        print("введены неверные данные")

    return item


b=selectBases()
a=selectAct()

if a == 1:
    ''' создание и добавление в сессию объектов классов  User и Dept'''
    r="y"
    while r == "y":
        addeditem = addItem(b)
        session.add(addeditem)
        r=input("хотите добавить еще одну запись? (y/n):")


elif a == 2:
    pass

session.commit()
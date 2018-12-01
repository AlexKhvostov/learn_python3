from builtins import print

import sqlalchemy #начните работу с этой библиотеки
from datetime import date
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper, sessionmaker
from setting_sql import SQL

#Создаем подключение к базе данных с использованием логина и пароля
engine = create_engine(SQL.settingSQL)
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




def selectTable():
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
    while (nAct != 1) and (nAct != 2) and (nAct != 3) and (nAct != 4):
        nAct = int(input("----------------------------------\n"
                         "| Выберите действие для обработки: \n"
                          "| 1 - добавить запись.  \n" #  def addItem
                          "| 2 - удалить запись \n" # def _____
                          "| 3 - редакитировать запись \n"
                          "| 4 - просмотреть записи \n"  # def seetable
                          "| Ваш выбор : "))
    return(nAct)


def probel(l=0, n=8):
    a = ""
    for i in range(l, n):
        a += " "
    return a

def tire(n):
    a = ""
    for i in range(n):
        a += "-"
    return a

def seetable(tabl): # принимает таблицу


    if tabl == 1:
        print(tire(25))
        for id, name in session.query(Dept.id, Dept.name):
            print("|", id, "|", name, probel(len(str(name)), 15),"|")
        print(tire(25))
    elif tabl ==2:
        print(tire(74))
        for instance in session.query(Workers).order_by(Workers.id):
            #name = session.query(Dept.name).filter(Dept.id == instance.deptname)
            for name in session.query(Dept.name).filter(Dept.id == instance.deptname):
                pass
                #print("|", name, "|")
            print("|",
                  instance.id,       probel(len(instance.fullname), 4), "|",
                  instance.fullname, probel(len(instance.fullname), 14), "|",
                  instance.birthday, probel(len(instance.birthday), 11), "|",
                  instance.salary,   probel(len(str(instance.salary)), 5), "|",
                  instance.deptname, probel(len(instance.deptname), 3), "|",
                  name[0],           probel(len(name[0]), 15), "|")
        print(tire(74))
    else:
        pass



def useBases(n):
    pass

def addItem(table):
    if table == 1:
        print("-------------\n Добавляем запись в таблицу 'отделы'.")
        deptname=input("Введите название отдела:")
        item = Dept(deptname)
    elif table == 2:
        print("-------------\n Добавляем запись в таблицу 'сотрудники'.")
        exitwhile = 0
        while exitwhile == 0:
            seetable(1)
            deptname = input("Выберите название отдела(число до 10): ") # должны дергаться из базы . решить перебором через if.

            for i in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10"):
                if i == deptname:
                    exitwhile = 1
            if exitwhile == 0:
                print("введено неверное значение, попробуйте еще раз:")

        fullname = input("Введите имя сотрудника: ")
        birthday = input("Введите дату рождения: ")
        salary = int(input("Ввдите зарплату сотрудника: "))
        item = Workers(deptname, fullname, birthday, salary)
    else:
        print("введены неверные данные")

    return item

def editItem(tabl):
    print("---------------------------------------")
    seetable(tabl)
    delID = int(input("введите id редактируемой записи:"))

    if tabl == 1:
        newname = input("Введите новое имя отдела : ")
        session.query(Dept).filter(Dept.id == delID).update({"name": newname})
        #print(session.query(Dept).filter(Dept.id == delID).name)
        seetable(tabl)
    elif tabl == 2:
        for instance in session.query(Workers).filter(Workers.id == delID):
            print(tire(13))
            print("Редактируем:")
            print(tire(13))

            print(tire(40))

            print('| Порядковый номер: ',instance.id, probel(len(str(instance.id)), 15), "|", end=" -> ")
            newid = input("новое значение :  ")
            print('|       Полное имя: ',instance.fullname, probel(len(instance.fullname), 15), "|", end=" -> ")
            newfullname = input("новое значение :  ")
            print('|    День рождения: ',instance.birthday, probel(len(instance.birthday), 15), "|", end=" -> ")
            newbirthday= input("новое значение :  ")
            print('|         Зарплата: ',instance.salary, probel(len(str(instance.salary)), 15), "|", end=" -> ")
            newsalary= input("новое значение :  ")
            print('|     Номер отдела: ',instance.deptname, probel(len(instance.deptname), 15), "|", end=" -> ")
            newdeptname= input("новое значение :  ")
            print(tire(40))

            #newid,newfullname,newbirthday,newsalary, newdeptname = input("")

            if newid == "":
                pass
            else:
                pass
                session.query(Workers).filter(Workers.id == delID).update({"id": newid})

            if newfullname == "":
                pass
            else:
                pass
                session.query(Workers).filter(Workers.id == delID).update({"fullname": newfullname})

            if newbirthday == "":
                pass
            else:
                pass
                session.query(Workers).filter(Workers.id == delID).update({"birthday": newbirthday})

            if newsalary == "":
                pass
            else:
                pass
                session.query(Workers).filter(Workers.id == delID).update({"salary": newsalary})

            if newdeptname == "":
                pass
            else:
                pass
                session.query(Workers).filter(Workers.id == delID).update({"deptname": newdeptname})

        pass
        #print(session.query(Workers).filter(Workers.id == delID).delete())
    else:
        pass

def delItem (tabl):
    print("---------------------------------------")
    seetable(tabl)
    delID = int(input("введите id удаляемой записи:"))
    # session.query(Workers).filter(Workers.id == delID).delete()

    if tabl == 1:
        session.query(Dept).filter(Dept.id == delID).delete()
    elif tabl == 2:
        session.query(Workers).filter(Workers.id == delID).delete()
    else:
        pass

endprogramm = "y"

while (endprogramm == "y") or (endprogramm == "д"):
    tabl = selectTable()
    action = selectAct()

    if action == 1:
        ''' создание и добавление в сессию объектов классов  User и Dept'''
        r = "y"
        while r == "y":
            addeditem = addItem(tabl)
            session.add(addeditem)
            r=input("хотите добавить еще одну запись? (y/n):")


    elif action == 2:
        delItem(tabl)
    elif action == 3:
        editItem(tabl)
    elif action == 4:
        seetable(tabl)



    session.commit()
    endprogramm = input("Повторить? (y/n) (д/н)? : ")
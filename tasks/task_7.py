'''
Написать функцию date принимающую день месяц и год.
вернуть True, если такая дата есть в нашем календаре. и False если такеой даты не существует
'''
import datetime

def date(d,m,y):
    true_date='True'
    try:
        datetime.date(y,m,d)
    except ValueError:
        true_date = 'False'
    return true_date


y=int(input('введите год: '))
m = int(input('введите месяц: '))
d = int(input('введите день: '))
print('дата ',d,'.',m,'.',y,' существует? - ',date(d,m,y),sep='')


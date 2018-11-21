'''
написать функцию is_year_leap определяющую высокосный ли введенный год.


'''
def is_year_leap(year):
    if year % 4 != 0:
        return 'обычный год'
    elif year % 100 == 0:
        if year % 400 == 0:
            return 'год высокосный'
        else:
            return 'обычный год'
    else:
        return 'год высокосный'


y = int(input('Введите номер года для определения високосный ли он : '))
print(is_year_leap(y))

''''

y = int(input())
if y % 4 != 0:
    print("Обычный")
elif y % 100 == 0:
    if y % 400 == 0:
        print("Високосный")
    else:
        print("Обычный")
else:
    print("Високосный")

# 2-й вариант:

if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
    print("Обычный")
else:
    print("Високосный")
    
'''

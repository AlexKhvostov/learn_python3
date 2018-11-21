'''
Написать функцию square, принимающую 1 аргумент - сторону квадрата и возвращающую три значчени с помощью картежа.
Периметр квадрата , площадь и диаганаль
'''
#from math import sqrt;
import math

def square(a):
    s=a*a

    p=a+a+a+a
    d=math.sqrt(a*a+a*a)
    print(s,p,d)
    return [s,p,d]

a=int(input('введите сторону квадрата : '))
print(square(a))

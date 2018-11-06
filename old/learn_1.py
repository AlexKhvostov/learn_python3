import math
import time
name = input("Введите ваше имя: ")        
print(" Здравствуй, ", name)
print()
print("Попробуем решить квадратное уравнение вида ax^2+bx+c=0.")
a = int(input("Введите атребуты a: "))
b = int(input("Введите атребуты b: "))
c = int(input("Введите атребуты c: "))
#print("a = ",a,", b = ",b,", c = ",c)
D=b*b -4*a*c
print()
print("Дискриминант равен ", D,";")
print()
if D>0:
    x1=(-b+math.sqrt(D))/(2*a)
    x2=(-b-math.sqrt(D))/(2*a)
    print("D>0, следовательно уравнение имеет 2 различных корня:")
    print("x1=", x1, "; x2=", x2,";")
elif D==0:
    x=(-b+math.sqrt(D))/(2*a)
    print("D=0, следовательно уравнение имеет 1 корень:")
    print("x=", x,";")
else:
    print("D<0, следовательно уравнение не имеет корней")

time.sleep(3)
print()
print("Спасибо за внимание!")
time.sleep(2)
print()
print("Досвидания!")
time.sleep(2)

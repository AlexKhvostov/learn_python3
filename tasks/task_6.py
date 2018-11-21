'''
написать функцию is_prime , принимающую значение от 1 до 1000 и определяющее простое ли число
если простое выводит True, евли не просто то выводит False.

'''

def is_prime(a):
    k=int(0)
    for i in range(a):
        if a % (i+1) == 0:
            k=k+1


        #k = k+1 if a % (i+1) ==0 else k=k*1

    if k <= 2:
        return 'True'
    else:
        return 'False'


def is_print(a):
    print('число',a,' простое - ',is_prime(a))

def is_line(numbers):
    for i in range(numbers):
        is_print(i+1)







a=int(input('Введите чилсо для определения является ли оно простым числом: '))
b=int(input('Введите последнее число рядка чисел кторые нужно рповерить на простоту: '))
is_print(a)
is_line(b)
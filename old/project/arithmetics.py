print('Простейшие арифметические операции')
print()
print('Если третий аргумент +, сложить их;\nесли —, то вычесть; * — умножить; / — разделить (первое на второе).\nВ остальных случаях вернуть строку "Неизвестная операция".')
print()
print()
a = int(input('Введите первое число: '))
b = int(input('Введите второе число: '))
c = input('Введите аргумент: ')
arithmetic = int()
if c == '+':
    arithmetic = a+b
    print('Сумма равна: ',arithmetic)
    print()
    print('Спасибо за внимание!')
elif c == '-':
    arithmetic = a-b
    print('Разность равна: ',arithmetic)
    print()
    print('Спасибо за внимание!')
elif c == '*':
    arithmetic = a*b
    print('Произведение равно: ',arithmetic)
    print()
    print('Спасибо за внимание!')
elif c == '/':
    arithmetic = a/b
    print('Частное равно: ',arithmetic)
    print()
    print('Спасибо за внимание!')
else:
    print()
    print('НЕИЗВЕСТНАЯ ОПЕРАЦИЯ!!!')
    print()
    print('Попробуйте ещё раз, при этом верно укажите аргумент!')




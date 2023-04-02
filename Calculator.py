from math import sqrt
print('\tЗапуск программы Калькулятор!\nКалькулятор может принимать только цифры')
a = input('Вкл - для включения;\tВыкл - для отключения;\nЧто сделать: ')
while a.title() == 'Вкл':
    b = input('Поддерживаемые оператор:\nсложение = +;\tвычитание = -;\tумножение = *;\tвозведение в степень = **;\tделение = /;\tцелочисленное деление = //;\t деление с остатком = %;\t корень = корень;\nКакой оператор использовать: ')
    if b == '+' or b == '-' or b == '*' or b == '**' or b == '/' or b == '//' or b == '%' or b == 'корень':
        if b == '+':
            b1 = input('Введите первое число: ')
            b2 = input('Введите второе число: ')
            while b1.isnumeric() == False:
                b1 = input('Введите первое число: ')
            while b2.isnumeric() == False:
                b2 = input('Введите второе число: ')
            if b1.isnumeric() == True and b2.isnumeric() == True:
                print(f'{b1} + {b2} = {int(b1) + int(b2)}')
        elif b == '-':
            b1 = input('Введите первое число: ')
            b2 = input('Введите второе число: ')
            while b1.isnumeric() == False:
                b1 = input('Введите первое число: ')
            while b2.isnumeric() == False:
                b2 = input('Введите второе число: ')
            if b1.isnumeric() == True and b2.isnumeric() == True:
                print(f'{b1} - {b2} = {int(b1) - int(b2)}')
        elif b == '*':
            b1 = input('Введите первое число: ')
            b2 = input('Введите второе число: ')
            while b1.isnumeric() == False:
                b1 = input('Введите первое число: ')
            while b2.isnumeric() == False:
                b2 = input('Введите второе число: ')
            if b1.isnumeric() == True and b2.isnumeric() == True:
                print(f'{b1} * {b2} = {int(b1) * int(b2)}')
        elif b == 'корень':
            b1 = input('Корень какого числа вы хотите извлечь: ')
            if int(b1) >= 0:
                    print(sqrt(int(b1)))
        elif b == '/':
            print('Помните, на ноль делить нельзя!')
            b1 = input('Введите первое число: ')
            b2 = input('Введите второе число: ')
            while b1.isnumeric() == False:
                b1 = input('Введите первое число: ')
            while b2.isnumeric() == False:
                b2 = input('Введите второе число: ')
            if b1.isnumeric() == True and b2.isnumeric() == True:
                while b2 == '0':
                    b2 = input('Введите второе число: ')
                    while b2.isnumeric() == False:
                        b2 = input('Введите второе число: ')
            if b2 != 0:
                print(f'{b1} / {b2} = {int(b1) / int(b2)}')
        elif b == '**':
            b1 = input('Введите первое число: ')
            b2 = input('Введите второе число: ')
            print(f'{b1} ** {b2} = {int(b1) ** int(b2)}')
        elif b == '//':
            print('Помните, на ноль делить нельзя!')
            b1 = input('Введите первое число: ')
            b2 = input('Введите второе число: ')
            while b1.isnumeric() == False:
                b1 = input('Введите первое число: ')
            while b2.isnumeric() == False:
                b2 = input('Введите второе число: ')
            if b1.isnumeric() == True and b2.isnumeric() == True:
                while b2 == '0':
                    b2 = input('Введите второе число: ')
                    while b2.isnumeric() == False:
                        b2 = input('Введите второе число: ')
            while b2 == '0':
                b2 = input('Введите второе число: ')
            if b2 != 0:
                print(f'{b1} // {b2} = {int(b1) // int(b2)}')
        elif b == '%':
            print('Помните, на ноль делить нельзя!')
            b1 = input('Введите первое число: ')
            b2 = input('Введите второе число: ')
            while b1.isnumeric() == False:
                b1 = input('Введите первое число: ')
            while b2.isnumeric() == False:
                b2 = input('Введите второе число: ')
            if b1.isnumeric() == True and b2.isnumeric() == True:
                while b2 == '0':
                    b2 = input('Введите второе число: ')
                    while b2.isnumeric() == False:
                        b2 = input('Введите второе число: ')
            while b2 == '0':
                b2 = input('Введите второе число: ')
            if b2 != 0:
                print(f'{b1} % {b2} = {int(b1) % int(b2)}')
        else:
            print('Вы ввели неккоректные данные')
if a.title() == 'Выкл':
    print('Возвращайтесть')
else:
    print('Я тебя не понимаю')
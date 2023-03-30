from math import sqrt
print('\tКалькулятор')
a1 = int(input('Введите первое число: '))
a2 = int(input('Введите второе число: '))
a3 = input('Введите оператор: ')
if a3 == '+':
    print(f'{a1} + {a2} = {a1 + a2}')
elif a3 == '-':
    print(f'{a1} - {a2} = {a1 - a2}')
elif a3 == 'корень':
    print(sqrt(a1),'\t',sqrt(a2))
elif a3 == '*':
    print(f'{a1} * {a2} = {a1 * a2}')
elif a3 == '**':
    print(f'{a1} ** {a2} = {a1 ** a2}')
elif a3 == '/' and a2 != 0:
    print(f'{a1} / {a2} = {a1 / a2}')
elif a3 == '//' and a2 != 0:
    print(f'{a1} // {a2} = {a1 // a2}')
elif a3 == '%' and a2 != 0:
    print(f'{a1} % {a2} = {a1 % a2}')
while a3 == '/' and a2 == 0:
    print('\tНа ноль делить нельзя!')
    a2 = int(input('Введите второе число заново: '))
    if a2 == 0:
        print()
    if a2 != 0:
        print(f'{a1} / {a2} = {a1 / a2}')
while a3 == '//' and a2 == 0:
    print('\tНа ноль делить нельзя!')
    a2 = int(input('Введите второе число заново: '))
    if a2 == 0:
        print()
    if a2 != 0:
        print(f'{a1} // {a2} = {a1 // a2}')
while a3 == '%' and a2 == 0:
    print('\tНа ноль делить нельзя!')
    a2 = int(input('Введите второе число заново: '))
    if a2 == 0:
        print()
    if a2 != 0:
        print(f'{a1} % {a2} = {a1 % a2}')
try:
    a = int(input('enter first number : '))
    b = int(input('enter second number :'))

    c = a/b
    print(f'{a} / {b} = ',c)
except ZeroDivisionError:
    print('cant divided by zero')
except ValueError:
    print('can only input numeric value')
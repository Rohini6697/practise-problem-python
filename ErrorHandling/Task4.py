try:
    n = int(input('enter a number : '))
    if n<0:
        raise ValueError
    print('valid positive number')
except ValueError:
    print('negetive number not valid')

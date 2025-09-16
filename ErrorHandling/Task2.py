try:
    age = int(input('enter your age : '))
    if age<0:
        raise ValueError('age should not be negative')

    print(f'age of the user is {age}')
    
except ValueError:
    print('age should be numeric')


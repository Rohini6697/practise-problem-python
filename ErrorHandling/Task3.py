list = ['apple','pineapple','banana']
try:
    index = int(input('enter the input : '))
    print(f'value of index {index} is {list[index]}')
except IndexError:
    print('element not found')
except ValueError:
    print('index should be integer')
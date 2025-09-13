import random
z = ['@','#','$','&','*']

def username(name):
    x = name.split()
    # print(x)
    y = random.choice(x)
    # print(y)
    k = random.choice(z)
    # print(k)
    number = str(random.randint(11111,9999999))
    # print(number)
    username = y+k+number
    print('your username is : ',username,end='')
name = input('enteryour name : ')
username(name)
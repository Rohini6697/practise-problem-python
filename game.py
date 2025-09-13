import random
def game(guess):
    x = random.randint(1,100)
    print(x)
    if(x == guess):
        print('you guesssed right')
    else:
        print('try again')
n = int(input('enter a no between 1 and 100 : '))
game(n)
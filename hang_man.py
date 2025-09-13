import random


words = {'python':'A popular programming language used for AI, web, and data analysis.','elephant':'The largest land animal with a trunk.','volcano':'A mountain that can erupt lava and ash'}

x,y = random.choice(list((words.items())))
print(y)

attepmpt = len(x)

hide = ['__']*len(x)
print(hide)

    # print('__ ',end='')
s = input('enter your guess first letter : ')
while(attepmpt>0):
    for ch in range(len(x)):
        if x[ch] == s:
            hide[ch] = s 
            attepmpt -=1
        else:
            print('try again')
    print(hide)
# def hangman(guess):
    
#     x = list(words.keys())
#     # print((x))
#     # print(x[0])

#     y = list(words.values())
#     print(y[0])
#     for ch in x[0]:
#         print('__   ',end='')
# g = input('enter your guess : ')
# hangman(g)
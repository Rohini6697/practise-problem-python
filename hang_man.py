import random


words = {'python':'A popular programming language used for AI, web, and data analysis.','elephant':'The largest land animal with a trunk.','volcano':'A mountain that can erupt lava and ash'}

x,y = random.choice(list((words.items())))
print('Clue : ',y)
hide = ['__']*len(x)
attempt = len(x)

while attempt>0:
    print(hide,'                 ','chances left :',attempt)
    s = input('enter your guess first letter : ')
    for ch in range(len(x)):
        if x[ch] == s:
            hide[ch] = s 
            print('Correct Guess')
    if s not in x:
        attempt -=1
        print('Wrong Guess')
    
    if '__' not in hide:
        print('You Win! The word is :',x)
        break
else:
    print('You Lose! The word is :',x)
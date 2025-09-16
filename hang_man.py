import random


words = {'python':'A popular programming language used for AI, web, and data analysis.','elephant':'The largest land animal with a trunk.','volcano':'A mountain that can erupt lava and ash'}

x,y = random.choice(list((words.items())))
print('Clue : ',y)
hide = ['__']*len(x)
attempt = len(x)

while attempt>0:
    print(' '.join(hide),'            ','chances left :',attempt)
    s = input('enter a letter : ').lower()

    if len(s)!=1 or not s.isalpha():
        print('please enter only one letter')
        continue
    if s in x:
        if s in hide:
            print('you already have guessed that letter')
            continue
        for ch in range(len(x)):
            if x[ch] == s:
                hide[ch] = s 
    else:
        attempt -=1
        print('Wrong Guess')
    
    if '__' not in hide:
        print()
        print('You Win! The word is :',x)
        break
else:
    print()
    print('You Lose! The word is :',x)
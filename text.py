import re
def text_analyzer(text):
    y = 0
    x = text.split()
    words = len(x)
    print('number of words : ',words)
    for i in x:
        for j in i:
            print(y)
            # print(x)
            y +=1
    print('number of characters : ',y)
    z = re.split(r'[.!?]',text)
    print(z)
    print('number of sentences : ',len(z)-1)
text = input('enter text : ')
text_analyzer(text)
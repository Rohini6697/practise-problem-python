import random
# while True:
mark = 0
try:
    with open('quiz.txt','r') as f:
        quiz = f.readlines()
        
        for i in len(quiz):

            quizes = random.choice(quiz)
            parts = quizes.strip().split(',')
            if len(parts) == 2:
                question,answer = parts
                print("Q : ",question)


except FileNotFoundError:
    print('file not found')

    

    answers = input('A : ')

    if answers.lower() == answer.lower():
        mark +=1
        print(f'Right Answer        {mark}')
    
    else:
        print('wrong answer')
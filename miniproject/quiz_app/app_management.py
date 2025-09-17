import random
# while True:
mark = 0
with open('quiz.txt','r') as f:
    quiz = f.readlines()
    random.shuffle(quiz)
    for quizes in range(len(quiz)):
        # score = 0
        parts = quiz[quizes].strip().split(',')
        if len(parts) == 2:
            question,answer = parts
            print("Q : ",question)

        answers = input('A : ')

        if answers.lower() == answer.lower():
            mark +=1
            print('Right Answer')
            
        else:
            print(f'wrong answer      correct answer : {answer}')
    print()
    print(f'Total Score : {mark}')
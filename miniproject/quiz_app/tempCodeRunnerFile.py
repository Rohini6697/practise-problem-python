    quizes = random.choice(quiz)
                parts = quizes.strip().split(',')
                if len(parts) == 2:
                    question,answer = parts
                    print("Q : ",question)


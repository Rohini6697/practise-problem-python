def add_record():
    with open('students.txt','a') as f:
        # data = f.readlines()

        name = input('enter student name : ')
        mark = input(f'enter {name}s mark : ')

        record = f'{name},{mark}'
        f.write(record)

def view_record():
    with open('students.txt','r') as f:
        data = f.readlines()

        for line in data:
            parts = line.strip().split(',')
            if len(parts) == 2:
                student,mark = parts
                print()
                print(f'student name : {student}')
                print(f'mark : {mark}')

def average_mark():
    with open('students.txt','r') as f:
        data = f.readlines()

        total = 0
        for line in data:
            parts = line.strip().split(',')
            if len(parts) == 2:
                student,marks = parts
                total += int(marks) 
        average = total/len(line)
        print(f'average mark : {average}')

def top_scorer():
    with open('students.txt','r') as f:
        data =f.readlines()

        largest = 0
        for line in data:
            parts = line.strip().split(',')
            if len(parts) == 2:
                student,mark = parts
                mark = int(mark)
                if int(mark) > largest:
                    largest = mark
                    top_scorer_student = student
                    # print(largest)
        
        if largest >=0:
            print(f'top scorer is {top_scorer_student} who scored {largest}')
        
    


while True:
    print()
    print('1. Add new student records')
    print('2. View all student records')
    print('3. Calculate average marks')
    print('4. Display the top scorer')
    print('5. Exit the program')
    print()

    choice = input('enter your choice : ')

    if choice == '1':
        add_record()
    elif choice == '2':
        view_record()
    elif choice == '3':
        average_mark()
    elif choice == '4':
        top_scorer()
    elif choice == '5':
        break
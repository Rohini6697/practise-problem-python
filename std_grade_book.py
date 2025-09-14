dictionary = {}

while True:
    print('GRADE CARD MENU : ')
    print('1.Add Student Name and Grade ')
    print('2. View Students and Grade')
    print('3. Average Grade')
    print('4. Heighest Grade')
    print('5. Lowest Grade')

    print()

    choice = input('Enter your choice :')
    print()

    if choice == '1':
        name = input('Enter Student Name : ').lower()
        grade = int(input('Enter Student Grade : '))
        dictionary[name] = grade
        print('student and grade added')
    elif choice == '2':
        print(dictionary)
    elif choice == '3':
        average = sum(dictionary.values())/len(dictionary)
        print('Average grade :',average)
    elif choice == '4':
        if dictionary != {}:
            highest = max(dictionary.values())
            print('Heighest Grade : ',highest)
        else:
            print('No grades available')
    elif choice == '5':
        if dictionary != {}:
            lowest = min(dictionary.values())
            print('Lowest Grade : ',lowest)
        else:
            print('No grades available')
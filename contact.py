dictionary = {}

while True:
    print('CONTAT MENU :')
    print()
    print('1. View Contacts')
    print('2. Add Contact')
    print('3. Delete Contact')
    print('4. Update Contact')
    print()

    value = input('enter your choice : ')
    if value == '1':
        print('contacts : ',dictionary)
    elif value == '2':
        name = input('Enter the name : ').lower()
        number = input('Enter the number : ').lower()
        dictionary[name] = number
        print('Contact Added')
    elif value == '3':
        name = input('enter the name want to delete : ').lower()
        if name in dictionary:
            dictionary.pop(name)
    elif value == '4':
        while True:
            print('UPDATE MENU : ')
            print('1. Update Name')
            print('2. Update Number')
            print('3. Exit')

            update_choice = input('enter your choice : ')

            
            if update_choice == '1':
                old_name = dictionary[name]
                

                old_name = input('enter the name want to update : ').lower()
                if old_name in dictionary:
                    new_name = input('updated name : ').lower()
                    dictionary[new_name] = number
                    dictionary.pop(old_name)
                    print(old_name,'updated')
                else:
                    print('Contact not found')
            elif update_choice == '2':
                # old_number = dictionary[number]

                update_name = input('enter whose number want to update : ').lower()
                if update_name in dictionary:
                    new_number = input('updated number : ').lower()
                    dictionary[update_name] = new_number
                    # dictionary.pop(old_number)
                    print(update_name,' number updated')
                else:
                    print('number not found')
            elif update_choice == '3':
                break
        
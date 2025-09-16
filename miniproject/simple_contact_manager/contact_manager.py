def add_contact() :
    with open('contact.txt','a') as f:
        user_name = input('enter the contact name : ')
        user_number = input('enter the contact number : ')
        user_email = input('enter email id : ')
        print()
        data = f'{user_name},{user_number},{user_email}'
        # data = f'name : {user_name} \nphone number : {user_number} \nemail id : {user_email}\n'
        f.write(data+'\n')

def search_contact():
    search = input('search : ')
    with open('contact.txt','r') as f:
        for line in f:
            name,number,email = line.strip().split(",")
            if search.lower() in name or search in number or search.lower() in email:
                print(name)
                print(number)
                print(email)

def show_contact():
    with open('contact.txt','r') as f:
        for line in f:
            name,number,email = line.strip().split(",")
            print(f'name : {name}')
            print(f'number : {number}')
            print(f'email : {email}')


def remove_contact():
    remove_name = input('enter the contect wanted to remove :')
    with open('contact.txt','r') as f:
        for line in f:
            name,number,email = line.strip().split(",")
            if name == remove_name:
                continue
            else:
                print(name)
                print(number)
                print(email)
while True:
    print('1. Add a contact')
    print('2. View all contacts')
    print('3. Search contact by name')
    print('4. Remove a contact')
    print('5. Exit the program')
    print()

    choice = input('enter your choice')

    if choice == '1':
        add_contact()
    elif choice == '2':
        show_contact()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        remove_contact()
    elif choice == '5':
        break

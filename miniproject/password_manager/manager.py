with open('passwords.txt','r') as f:
    passwords = f.readlines()

    for line in passwords:
        parts = line.strip().split(',')
        if len(parts) == 3:
            website,username,password = parts



def add_credentials():
    with open('passwords.txt','a') as f:
        add_website = input('enter website name : ')
        add_username = input('enter usename : ')
        add_password = int(input('enter password : '))
        print()
        add_data = f'{add_website},{add_username},{add_password}'
        f.write(add_data+'\n')


def veiw_credentilas():
    with open('passwords.txt','r') as f:
        passwords = f.readlines()
        parts = line.strip().split(',')
        if len(parts) == 3:
            website,username,password = parts
        print()
        print(f'website : {website}')
        print(f'username : {username}')
        print(f'password : {password}')

def search_credentials():
    with open('passwords.txt','r') as f:
        passwords = f.readlines()
        search = input('search : ')
        for line in passwords:
            parts = line.strip().split(',')
            if len(parts) == 3:
                website,username,password = parts

            
                if search.lower() in website.lower():
                    print('website found')
                    print()
                    print(f'website : {website}')
                    print(f'user name : {username}')
                    print(f'password : {password}')
                    print()
                else:
                    print('website not found')
while True:
    print('1. Add new credentials')
    print('2. View credentials for a specific website')
    print('3. View all stored credentials')
    print('4. Exit the program')
    print()


    choice = input('enter your choice : ')

    if choice == '1':
        add_credentials()
    elif choice == '2':
        search_credentials()
    elif choice == '3':
        veiw_credentilas()
    elif choice == '4':
        break
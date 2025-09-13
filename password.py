def password(password):
    if password == '':
        print('needed to enter password')
    if len(password)>8:
        print('the password should be less tthan 8')
    if not any(ch.isupper() for ch in password):
        print('needed uppercase')
    if not any(ch.islower() for ch in password):
        print('needed lowercase')
    if any(ch.isalnum() for ch in password):
        print('add special charactes too')
    if not any(ch.isdigit() for ch in password):
        print('needed numbers')

word = input('enter password : ')
password(word)
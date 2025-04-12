from auth import *
from crypto_utils import *
from src import *
while True:

    print('Welcome to the password manager. Type R to register, S to sign in, or Q to quit.')
    user_input = input('> ').strip().lower()

    if user_input == 'q':
        break
    elif user_input == 'r':
        print('Please enter your master password.')
        pwd = input('> ').strip().lower()
    elif user_input == 's':
        print('Please set your master password.')
        pwd = input('> ').strip().lower()
        register_master_password(pwd)
    else:
         print('Incorrect command entered exiting program.')
         break
        
    while not check_login(pwd):
        print('Your master password is wrong, please enter the correct master password.')
        pwd = input('> ').strip().lower()
    
    while True:
        print('Thank you for logging in. Type S to search for a credential, A to add a credential, E to edit a credential, or D to delete a credential')
        user_input = input('> ').strip().lower()
        if user_input == 's':
            print('Enter the service.')
            serv = input('> ').strip().lower()
            out = search_by_service(serv)
            if out == None:
                print('That service does not exist.')
            else:
                print(f"Username: {out[0]}\n, Password: {out[1]}")

        elif user_input == 'a':
            print('Enter the service.')
            serv = input('> ').strip().lower()
            print('Enter the username.')
            un = input('> ').strip().lower()
            cred_pw = input('> ').strip().lower()
            add_new_credential(serv, un, cred_pw)

        elif user_input == 'e':
            print('Enter the service to edit.')
            serv = input('> ').strip().lower()
            print('Enter the username.')
            un = input('> ').strip().lower()
            cred_pw = input('> ').strip().lower()
            add_new_credential(serv, un, cred_pw)

        elif user_input == 'd':



    










    
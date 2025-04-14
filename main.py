from auth import *
from crypto_utils import *
from src import *

try:
    

    if set_up_json('storage.json')
    print('Welcome to the password manager.  \nType R to register, S to sign in. To quit and log out at any time, press (control + C).')
    while True:
        user_input = input('> ').strip().lower()

        if user_input == 'q':
            break
        elif user_input == 'r':
            print('Please register your master password by typing it below.')
            pwd = input('> ').strip().lower()
            register_master_password(pwd)
        elif user_input == 's':
            print('Please sign in with your master password.')
            pwd = input('> ').strip().lower()
        else:
            print('Incorrect command entered exiting program.')
            break
            
        while not check_login(pwd):
            print('Your master password is wrong, please enter the correct master password or press (control + C) to log out exit.')
            pwd = input('> ').strip().lower()
        
        print('Thank you for logging in.')
        while True:

            
            print('Type S to search for a credential. \nA to add a credential. \nE to edit a credential. \nD to delete a credential')
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

                print('Enter the password.')
                cred_pw = input('> ').strip().lower()
                add_new_credential(serv, un, cred_pw)
                print('Credential added.')

            elif user_input == 'e':
                print('Enter the service to edit.')
                serv = input('> ').strip().lower()

                out = search_by_service(serv)
                if out == None:
                    print('That service does not exist.')
                else:
                    print('Do you want to change the username or password? \nType U for username and P for password.')
                    change = input('> ').strip().lower()

                    if change == 'u':
                        print('Enter the new username.')
                        new_un = input('> ').strip().lower()
                        edit_credential_username(serv, new_un)
                        print(f'Username for {serv} edited.')
                        
                    elif change == 'p':
                        print('Enter the new password.')
                        new_pw = input('> ').strip().lower()
                        edit_credential_password(serv, new_pw)
                        print(f'Password for {serv} edited.')

                    else:
                        print('Invalid input. No edits made.')

            elif user_input == 'd':
                print('Enter the service to delete.')
                serv = input('> ').strip().lower()

                delete_credential(serv)
                print('Service deleted')

except KeyboardInterrupt:
    print("\n----------------------------------------------------\nLogging out and exiting the program.") 

        










        
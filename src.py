# CLI interface 
from auth import *
from crypto_utils import *
import json

## IDK SHOULD ALl OF THIS MAYBE GO INTO A DIFF FILE??? 

storage_filename = 'storage.json'
#set up json file so everything goes into the "credentials" object
# gets called when someone initializes their master password
def set_up_json(filename): 
    #json skeleton
    data = {
        'master_password' : '',
        'credentials' : []
    }
    with open(filename, 'w') as file: 
        json.dump(data, file)

# actions 

# adds new service, username, password to password vault 
def add_new_credential(service, username, password): 
    # encrypt the password 
    encrypted_password = encrypt_password(password) #from crypto_utils 

    # prepare json list (index 0 -service, index 1- username, index 2 - password) 
    print(f"Password: {password} and encrypted: {encrypted_password}")
    credential = [service, username, encrypted_password]


    # add to the credentials in the json file, making sure to append instead of overwrite
    with open(storage_filename,'r') as file: 
        data = json.load(file)
    
    # append new credential
    data['credentials'].append(credential)

    # write into json file 
    with open(storage_filename, 'w') as file: 
        json.dump(data, file)

# returns a tuple (username, decrypted password)
def search_by_service(service): 
    # open json file 
    with open(storage_filename, 'r') as file: 
        data = json.load(file) 

    # search for correct service 
    for credential in data.get('credentials'): 
        if credential[0] == service: 
            username = credential[1]
            decrypted_password = decrypt_password(credential[2])
            return (username, decrypted_password)
    # none found 
    return None  

def retrieve_credential(service, username):
    pass


def edit_credential_username(service, new_username): 
    # open json file 
    with open(storage_filename, 'r') as file: 
        data = json.load(file) 

    # search for correct service and edit the password  
    for credential in data.get('credentials'): 
        if credential[0] == service: 
            credential[1] = new_username

    # Save the updated list back to the JSON file
    with open('storage.json', 'w') as file:
        json.dump(data, file, indent=4)

def edit_credential_password(service, new_password): 
    # open json file 
    with open(storage_filename, 'r') as file: 
        data = json.load(file) 

    # search for correct service 
    for credential in data.get('credentials'): 
        if credential[0] == service: 
            credential[2] = encrypt_password(new_password)

     # Save the updated list back to the JSON file
    with open('storage.json', 'w') as file:
        json.dump(data, file)

def delete_credential(service):
    target = None
     # open json file 
    with open(storage_filename, 'r') as file: 
        data = json.load(file) 

    # search for correct service 
    for credential in data.get('credentials'): 
        if credential[0] == service: 
            target = credential
    

    if target == None: 
        print("Service not found")
        return 
    
    # Remove it from the list
    if target in data.get('credentials'):
        data.get('credentials').remove(target)

    # Save the updated list back to the JSON file
    with open('storage.json', 'w') as file:
        json.dump(data, file)

def user_logout(user_input):
    if user_input == 'EXIT':
        return True
    else:
        return False


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

    # prepare json object 
    credential = [
        {
            'service' : 'service',
            'username' : 'username', 
            'password' : encrypted_password
        }
    ]

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
        if credential.get('service') == service: 
            username = credential.get('username')
            decrypted_password = decrypt_password(credential.get('password'))
            return (username, decrypted_password)
    # none found 
    return None  

def retrieve_credential(service, username):
    pass


def edit_credential_username(service, new_username): 
    # open json file 
    with open(storage_filename, 'r') as file: 
        data = json.load(file) 

    # search for correct service 
    for credential in data.get('credentials'): 
        if credential.get('service') == service: 
            credential['username'] = new_username

def edit_credential_password(service, new_password): 
    # open json file 
    with open(storage_filename, 'r') as file: 
        data = json.load(file) 

    # search for correct service 
    for credential in data.get('credentials'): 
        if credential.get('service') == service: 
            credential['password'] = encrypt_password(new_password.encode()).hexdigest()

def delete_credential(service):
     # open json file 
    with open(storage_filename, 'r') as file: 
        data = json.load(file) 

    # search for correct service 
    for credential in data.get('credentials'): 
        if credential.get('service') == service: 
            del data[credential]


# CLI interface 
from auth import *
from crypto_utils import *
import json

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

    # add to the credentials in the json file, making sure to append
    with open(storage_filename,'r') as file: 
        data = json.load(file)
    
    # append new credential
    data['credentials'].append(credential)

    # write into json file 
    with open(storage_filename, 'w') as file: 
        json.dump(data, file)


def search_by_service(service): 
    pass 

def retrieve_credential(service, username): 
    pass 

def edit_credential(service, username, new_password): 
    pass 

def delete_credential(service): 
    pass
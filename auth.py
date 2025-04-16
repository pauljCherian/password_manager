# master password set up and log in 
import hashlib 
import os 
import json
import base64
from crypto_utils import *

def is_vault_empty(vault):
    return vault.get('master_password') == ''

# if first time, generate a unique salt
def save_first_salt():
    try:
        with open('auth.json', 'r') as auth_file:
            auth_data = json.load(auth_file)
    except (json.JSONDecodeError, FileNotFoundError):
        auth_data = {}

    if 'salt' not in auth_data:
        salt = os.urandom(16)
        auth_data['salt'] = base64.b64encode(salt).decode()
        
        with open('auth.json', 'w') as auth_file: 
            json.dump(auth_data, auth_file, indent=4)

    # Decode the salt from base64
    return base64.b64decode(auth_data.get('salt'))


def register_master_password(master_password): 
    # Get the salt first
    salt = save_first_salt()
    
    # hash and salt the master password 
    hashed_salted_master = hashlib.sha256(salt + master_password.encode()).hexdigest()

    # store this in json file 
    with open('storage.json', 'r') as file: 
        data = json.load(file)

    # prepare for json storage 
    data['master_password'] = hashed_salted_master

    # store this in json file 
    with open('storage.json', 'w') as file: 
        json.dump(data, file)

# checks if the given master_password is the correct one 
# returns True if password matches, False otherwise 
def check_login(master_password_try): 
    # retrieve the salt 
    saved_salt = save_first_salt()

    # retrieve the actual master password from the json file 
    with open('storage.json', 'r') as file:
        data = json.load(file)

    master_password = data.get('master_password')  # this is hashed and salted

    # hash and salt the try 
    hashed_salted_try = hashlib.sha256(saved_salt + master_password_try.encode()).hexdigest()

    # compare to the actual master password
    if hashed_salted_try == master_password: 
        return True 
    else: 
        return False 

# master password set up and log in 
import hashlib 
import os 
import json
from main import first_time 
from crypto_utils import *

# check_login(username, password)
# Checks if username is valid 
# If not in storage.json return “user not found”/prompt to create a new account
# Checks if (username, hash(password)) is in storage.json
# Returns boolean if correct or not 
# add_new_user(username, master_password): 
# Hashes and salts the master_password using PBKDF2HMAC
# Stores username and master_password into a json file 

# generate a random salt if first time 
if first_time: 
    salt = os.urandom(16) #16 byte random salt 
    # encrypt the salt 
    encrypted_salt = encrypt_password(salt)
    # save the salt into auth.json
    # store this in json file 
    with open('auth.json', 'r') as file: 
        data = json.load(file)
    
    data['salt'] = encrypted_salt

    # store this in json file 
    with open('storage.json', 'w') as file: 
        json.dump(data, file)


def register_master_password(master_password): 
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
    # retrieve the actual master password from the json file 
    with open('auth.json', 'r') as file:
        salt_data = json.load(file)
    
    saved_salt = decrypt_password(data.get(salt))

    # retrieve the actual master password from the json file 
    with open('storage.json', 'r') as file:
        data = json.load(file)

    master_password = data.get('master_password')#this is hashed and salted

    # hash and salt the try 
    hashed_salted_try = hashlib.sha256(saved_salt + master_password_try.encode()).hexdigest()

    # compare to the actual master password
    if hashed_salted_try == master_password: 
        return True 
    else: 
        return False 

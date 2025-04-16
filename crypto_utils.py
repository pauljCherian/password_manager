# encryption and decryption logic 
from cryptography.fernet import Fernet
import json
import os
# make const encryption_key variable to remember the encryption key 
# add_encrypted_credential(service, username, password) 
# calls some encrypt function in cryptography library to encrypt service, username, password 
# Stores encrypted service, username, password in storage.json
# decrypt(json object)
# Use the encryption_key to decrypt and return the username and password 

def get_or_create_key():
    try:
        with open('auth.json', 'r') as auth_file:
            auth_data = json.load(auth_file)
            if 'encryption_key' in auth_data:
                return auth_data['encryption_key']
    except (json.JSONDecodeError, FileNotFoundError):
        auth_data = {}


    encryption_key = Fernet.generate_key().decode()
    auth_data['encryption_key'] = encryption_key

    with open('auth.json', 'w') as auth_file:
        json.dump(auth_data, auth_file, indent=4)
    
    return encryption_key


encryption_key = get_or_create_key().encode()
f = Fernet(encryption_key)

# only encrypt a password 
def encrypt_password(password): 
    token = f.encrypt(password.encode()).decode()
    return token  #encrypted bit string 

#decrypt some json object password 
def decrypt_password(encrypted_password): 
    password = f.decrypt(encrypted_password.encode()).decode()
    return password 
# master password set up and log in 
import bcrypt
import hashlib 
import os 
import json 

# check_login(username, password)
# Checks if username is valid 
# If not in storage.json return “user not found”/prompt to create a new account
# Checks if (username, hash(password)) is in storage.json
# Returns boolean if correct or not 
# add_new_user(username, master_password): 
# Hashes and salts the master_password using PBKDF2HMAC
# Stores username and master_password into a json file 

# generate a random salt 
salt = os.urandom()

def register_master_password(master_password): 
    pass 

# checks if the given master_password is the correct one 
# returns True if password matches, False otherwise 
def check_login(master_password_try): 
    # TODO: retrieve the actual master password from the json file 
    with open('storage.json', 'r') as file:
        data = json.load(file)

    master_password = data['master password'] #this is hashed and salted

    # hash the try  
    hashed_try = bcrypt.hashpw(master_password_try, salt)
    # salt the try 
    hashed_salted_try = hashlib.pbkdf2_hmac("sha256", hashed_try, salt, 10000)

    # compare to the actual master password
    if hashed_salted_try == master_password: 
        return True 
    else: 
        return False 

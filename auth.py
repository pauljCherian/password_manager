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
salt = os.urandom(16) #16 byte random salt 

def register_master_password(master_password): 
    # hash and salt the master password 
    hashed_salted_master = hashlib.pbkdf2_hmac("sha256", master_password, salt, 10000)

    # store this in json file 
    with open('storage.json', 'r') as file: 
        data = json.load(file)

    # prepare for json storage 
    data['master_password'].append(hashed_salted_master)

    # store this in json file 
    with open('storage.json', 'w') as file: 
        json.dump(data, file)

# checks if the given master_password is the correct one 
# returns True if password matches, False otherwise 
def check_login(master_password_try): 
    # retrieve the actual master password from the json file 
    with open('storage.json', 'r') as file:
        data = json.load(file)

    master_password = data.get('master_password') #this is hashed and salted

    # hash and salt the try 
    hashed_salted_try = hashlib.pbkdf2_hmac("sha256", master_password_try, salt, 10000)

    # compare to the actual master password
    if bcrypt.checkpw(hashed_salted_try, master_password): 
        return True 
    else: 
        return False 

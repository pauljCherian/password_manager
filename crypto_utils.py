# encryption and decryption logic 
from cryptography.fernet import Fernet
# Constant encryption_key variable to remember the encryption key 
# add_encrypted_credential(service, username, password) 
# calls some encrypt function in cryptography library to encrypt service, username, password 
# Stores encrypted service, username, password in storage.json
# decrypt(json object)
# Use the encryption_key to decrypt and return the username and password 


encryption_key = Fernet.generate_key()
f = Fernet(encryption_key)

# only encrypt a password 
def encrypt_password(password): 
    token = f.encrypt(password.encode()).decode()
    return token  #encrypted bit string 

#decrypt some json object password 
def decrypt_password(encrypted_password): 
    password = f.decrypt(encrypted_password.encode()).decode()
    return password 
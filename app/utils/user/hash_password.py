import hashlib

def get_hashed_password(password):
    hashed_password = hashlib.sha256(str(password).encode('utf-8'))
    return hashed_password.hexdigest()

def verify_password(plain_password, hashed_password):
    password = get_hashed_password(plain_password)
    return password == hashed_password

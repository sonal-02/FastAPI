import hashlib


class Password:
    """
    Password class is used to create hashed password and verify password is correct or not
    """

    def __init__(self, plain_password=None, hashed_password=None):
        self.plain_password = plain_password
        self.hashed_password = hashed_password

    def get_hashed_password(self):
        hashed_password = hashlib.sha256(
            str(self.plain_password).encode('utf-8'))
        return hashed_password.hexdigest()

    def verify_password(self):
        password = self.get_hashed_password()
        return password == self.hashed_password

import rsa
import os
import hashlib

from datetime import datetime

class EncryptionHandler:
    """Encryption handler class, that handles the encyrption/decryption of data"""
    public_keys, private_keys = rsa.newkeys(1024)
    public_path = "public.pem"
    private_path = "private.pem"
    created_public_keys = None
    created_private_keys = None

    def __init__(self):
        self.create_keys()

    def create_keys(self):
        if not os.path.exists(self.public_path):
            with open (self.public_path, "wb") as f:
                f.write(self.public_keys.save_pkcs1("PEM"))

        if not os.path.exists(self.private_path):
            with open (self.private_path, "wb") as f:
                f.write(self.private_keys.save_pkcs1("PEM"))
        

    def get_public_key(self):
        if os.path.exists(self.public_path):
            with open (self.public_path, "rb") as f:
                public_key = rsa.PublicKey.load_pkcs1(f.read())
                return public_key

    def get_private_key(self):
        if os.path.exists(self.private_path):
            with open (self.private_path, "rb") as f:
                private_key = rsa.PrivateKey.load_pkcs1(f.read())
                return private_key
            

    def encrypt_data(self, data):
        self.created_public_keys = self.get_public_key()
        encrypted_data = rsa.encrypt(data.encode(), self.created_public_keys)
        return encrypted_data

    def decrypt_data(self, data):
        self.created_private_keys = self.get_private_key()
        decrypted_data = rsa.decrypt(data, self.created_private_keys)
        return decrypted_data.decode()        

class HashHandler:
    """Hash handler class, that handles the hashing of data"""

    def hash_password(self, password):
        """Returns a hashed password"""
        hash_algortihm = hashlib.new("SHA256")
        hash_algortihm.update(password.encode())
        hashed_pass = hash_algortihm.hexdigest()
        return hashed_pass
    
    def compare_hashed_data(self, data, hashed_data):
        new_hash = self.hash_password(data)
        if(new_hash == hashed_data):
            return True
        return False

class DateHandler:

    def get_current_date_only(self):
        current_date = datetime.now().strftime("%d/%m/%Y")
        return current_date





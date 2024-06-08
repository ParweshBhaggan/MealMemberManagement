import datetime    
import random
import re  
import rsa     #pip install rsa
import hashlib     
import os          

class Validators:
    """Validation handler class, that handles the validation of inputs"""
    #public functions
    def create_id(sellf):
        """ Generates an unique ID based on certain criterias """
        current_datetime = datetime.datetime.now()
        current_year = current_datetime.year
        year_digit = current_year % 100
        year_text = str(year_digit)
        id = []
        digits = [i for i in range(10)]
        for i in range(10):
            if i < 2:
                id.append(year_text[i])
            if 2 < i < 9:
                random_digit = random.choice(digits)
                id.append(str(random_digit))
            if i == 9:
                sum = 0
                for j in range(8):
                    sum = sum + int(id[j])
                id.append(str((sum % 10)))
        id_digit = int("".join(id))
        return id_digit

    def valid_username(self, username):
        """ Validates the username based on certain criterias """
        username = str(username).lower()
        
        first_letters_array = [chr(ord('a') + i) for i in range(26)]
        first_letters_array.append("_")
        
        digit_chars = [str(i) for i in range(10)]
        
        valid_char_array = []
        
        for letter in first_letters_array:
            valid_char_array.append(letter)
        for digit in digit_chars:
            valid_char_array.append(digit)
        valid_char_array.append("'")
        valid_char_array.append(".")
        
        if not self._check_username_length(username):
            print("Username too long or too short")
            return False
        elif not self._check_first_character(username, first_letters_array):
            print("Incorrect 'first' letter")
            return False
        elif not self._check_username_chars(username, valid_char_array):
            print("Wrong username")
            return False
        return True



    def valid_password(self,password):
        """ Validates the password based on certain criterias """
        lower_chars = [chr(ord('a') + i) for i in range(26)]
        upper_chars = [chr(ord('A') + i) for i in range(26)]
        digit_chars = [str(i) for i in range(10)]
        
        
        special_char = r"~!@#$%&_-+=`|\(){}[]:;'<>,.?/"
        special_chars_array = []
        for i in range(len(special_char)):
            special_chars_array.append(special_char[i])

        if not self._check_password_length(password):
            print("Password too long or too short")
            return False
        elif not self._check_password_lower_char(password, lower_chars):
            print("Password has no lowercase character")
            return False
        elif not self._check_password_upper_char(password, upper_chars):
            print("Password has no uppercase character")
            return False
        elif not self._check_password_special_char(password, special_chars_array):
            print("Password has no valid special character")
            return False
        elif not self._check_password_digit(password, digit_chars):
            print("Password has no digit")
            return False
        
        return True
    
    def create_phone_numer(self, digits):
        """ Validates and creates a phone number based on certain criterias """
        if not self._check_valid_phone_digits(digits):
            return False
        text_digits = str(digits)
        number_prefix = "+31-6-"
        phone_number = number_prefix + text_digits
        return phone_number
    
    def check_valid_zipcode(self, zipcode):
        """ Validates the zipcode based on certain criterias """
        zipcode = str(zipcode).upper()
        upper_chars = [chr(ord('A') + i) for i in range(26)]
        
        if len(zipcode) != 6:
            return False

        text_chars_arr = []
        text_chars_arr.append(zipcode[4])
        text_chars_arr.append(zipcode[5])
        
        digit_chars_arr = []
        

        for i in range(4):
            digit_chars_arr.append(zipcode[i])
        
        digits = "".join(digit_chars_arr)
        text_chars = "".join(text_chars_arr)

        for char in text_chars:
            if char not in upper_chars:
                print("Wrong zipcode format text")
                return False
        
        try:
            digits = int(digits)
            return True
        except Exception as e:
            print("Wrong zipcode format DIGITS")
            return False
    
    def check_valid_age(self, age):
        """ Validates the age input based on certain criterias """
        input_age = age
        try:
            input_age = int(age)
            if not (0 < input_age <= 111):
                print("Incorrect age")
                return False
            return True
        except Exception as e:
            print("Incorrect age format")
            return False

    def check_valid_weigth(self, weight):
        """ Validates the weigth input based on certain criterias """
        input_weight = weight
        try:
            input_weight = int(weight)
            return True
        except Exception as e:
            print("Incorrect weight format")
            return False
    
    def check_valid_gender(self, gender):
        """ Validates the gender input based on predefined values """
        valid_genders = ['male', 'female', 'other', 'prefer not to say']
        return gender.lower() in valid_genders


    def check_valid_email(self, email):
        """ Validates the email input based on certain criterias """
        email_characters = ['@', '.']

        for char in email_characters:
            if char not in email:
                return False
        return True

    def check_null_bytes(self, input_string):
        """Checks for null_bytes"""
        if re.search(r'\x00', input_string):
            return True
        return False

    #Private Functions

    def _check_username_chars(self, username, valid_char_array):
        for char in username:
            if char not in valid_char_array:
                return False
        return True

    def _check_username_length(self, username):
        if not (8 <= len(username) <= 12):
            return False
        return True

    def _check_first_character(self, username, firstchar_array):
        first_character = username[0]
        if first_character not in firstchar_array:
            return False
        return True

    def _check_password_special_char(self, password, special_chars_array):
        for char in password:
            if char in special_chars_array:
                return True
        return False

    def _check_password_lower_char(self, password, lower_chars_array):
        for char in password:
            if char in lower_chars_array:
                return True
        return False

    def _check_password_upper_char(self, password, upper_chars_array):
        for char in password:
            if char in upper_chars_array:
                return True
        return False

    def _check_password_digit(self, password, digits_array):
        for char in password:
            if char in digits_array:
                return True
        return False

    def _check_password_length(self, password):
        if 12 <= len(password) <= 30:
            return True
        return False
     
    def _check_valid_phone_digits(self, text):
        try:
            digits = int(text)
            if not len(text) == 8:
                return False
            return digits
        except Exception as e:
            return False
        

class EncryptionHandler:
    """Encryption handler class, that handles the encyrption/decryption of data"""
    public_keys, private_keys = rsa.newkeys(1024)
    public_path = "public.pem"
    private_path = "private.pem"


    def create_keys(self, file_path_public = public_path, file_path_private = private_path):
        if not os.path.exists(file_path_public):
            with open (file_path_public, "wb") as f:
                f.write(self.public_keys.save_pkcs1("PEM"))

        if not os.path.exists(file_path_private):
            with open (file_path_private, "wb") as f:
                f.write(self.private_keys.save_pkcs1("PEM"))

    def get_public_key(file_path = public_path):
        if os.path.exists(file_path):
            with open (file_path, "rb") as f:
                public_key = rsa.PublicKey.load_pkcs1(f.read())
                return public_key

    def get_private_key(file_path = private_path):
        if os.path.exists(file_path):
            with open (file_path, "rb") as f:
                private_key = rsa.PrivateKey.load_pkcs1(f.read())
                return private_key
            

    def encrypt_data(data, public_key):
        encrypted_data = rsa.encrypt(data.encode(), public_key)
        return encrypted_data

    def decrypt_data(data, private_key):
        decrypted_data = rsa.decrypt(data, private_key)
        return decrypted_data.decode()        


class HashHandler:
    """Hash handler class, that handles the hashing of data"""

    def hash_password(self, password):
        """Returns a hashed password"""
        hash_algortihm = hashlib.new("SHA256")
        hash_algortihm.update(password.encode())
        hashed_pass = hash_algortihm.hexdigest()
        return hashed_pass


class Logger:
    """Logger class, that logs activities"""

    log_date = ""
    log_time = ""
    log_username= ""
    log_activity = ""
    log_info=""
    log_suspicion = ""

    def create_log(self, date, time, username, activity, info, suspicion):
        self.log_date = date
        self.log_time = time
        self.log_username = username
        self.log_activity = activity
        self.log_info = info
        self.log_suspicion = suspicion
        return self
        
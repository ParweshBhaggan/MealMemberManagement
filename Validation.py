import datetime    
import random
import re  

class Validators:
    """Validation handler class, that handles the validation of inputs"""
    
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
            print("Invalid username. Username must be 8-12 characters long.\n")
            return False
        elif not self._check_first_character(username, first_letters_array):
            print("Incorrect 'first' letter\n")
            return False
        elif not self._check_username_chars(username, valid_char_array):
            print("Invalid username. Username must be 8-12 characters long and can only contain letters, digits, underscores, apostrophes, and dots.\n")
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

    def ValidateNumber(self, number):
        if(len(number) == 14):
            return True
        print(f"Invalid mobile phone number. Mobile phone number must be 8 digits long.")
        return False
        
    
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
    @staticmethod
    def is_valid_street_name(street_name):
        """Validate that the street name contains only letters and spaces."""
        return bool(re.match(r"^[A-Za-z\s]+$", street_name))
    @staticmethod
    def is_valid_housenumber(housenumber):
        """Validate that the street number is a non-negative integer."""
        return housenumber.isdigit() and int(housenumber) >= 0
    
    def check_valid_age(self, age):
        """ Validates the age input based on certain criterias """
        
        input_age = age
        try:
            input_age = int(age)
            if (0 < input_age <= 111):
                return True
            print("Incorrect age")
            return False
        except Exception as e:
            print("Incorrect age format")
            return False

    def valid_firstname(self, firstname):
        return 2 <= len(firstname) <= 30 and firstname.replace(" ", "").replace("-", "").replace("'", "").isalpha()

    def valid_lastname(self, lastname):
        return 2 <= len(lastname) <= 30 and lastname.replace(" ", "").replace("-", "").replace("'", "").isalpha()

    def check_valid_weigth(self, weight):
        """Validates that the weight is between 3 and 250 kilograms."""
        try:
            weight = float(weight)
            if 3 <= weight <= 250:
                return True
            print("Invalid weight. Weight must be between 3 and 250 kilograms.")
            return False
        except ValueError:
            print("Invalid weight format. Weight must be a number.")
            return False
    
    def check_valid_gender(self, gender):
        """ Validates the gender input based on predefined values """
        valid_genders = ['male', 'female', 'other', 'prefer not to say']
        return gender.lower() in valid_genders

    def check_valid_email(self, email):
        """ Validates the email input based on certain criterias """
        regex = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if re.match(regex, email):
            return True
        print("Invalid email format.")
        return False

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
        

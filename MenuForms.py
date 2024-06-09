
from User import Consultant, SuperAdmin, SystemAdmin, User
from Members import Member
from UserServices import UserServices
from Validation import Validators
from termcolor import colored
import random
from Utilities import Utilities


class MenuForms:
    def __init__(self) -> None:
        self.validator = Validators()
        self.adressform = AddressForm()
        self.services = UserServices(User())
        self.utilities = Utilities()
        

    def UserForm(self, user):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("User Form")
   
        firstname = input("Enter Firstname: \n")
        while not self.validator.valid_firstname(firstname):
            print("Invalid firstname. Firstname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
            firstname = input("Enter Firstname again: \n")
        
        lastname = input("Enter Lastname: \n")
        while not self.validator.valid_lastname(lastname):
            print("Invalid lastname. Lastname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
            lastname = input("Enter Lastname again: \n")
        
        username = input("Enter Username: \n")
        while not self.validator.valid_username(username):
            print("Invalid username. Username must be 8-12 characters long and can only contain letters, digits, underscores, apostrophes, and dots.")
            username = input("Enter Username again: \n")

        password = input("Enter Password: \n")
        while not self.validator.valid_password(password):
            print("Invalid password. Password must be 12-30 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character.")
            password = input("Enter Password again: \n")
       
        # Creating the user object based on its type
        name = user.__class__.__name__
        if(name == "SystemAdmin"):
            user = SystemAdmin(firstname, lastname, username, password)
        elif(name == "Consultant"):
            user = Consultant(firstname, lastname, username, password)
        print(f"Added User: {user.firstname} {user.lastname} {user.typeUser}")
        self.utilities.SleepConsole(1.1)
        return user

    def MemberForm(self):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Member Form")
  
        firstname = input("Enter Firstname: \n")
        while not self.validator.valid_firstname(firstname):
            print("Invalid firstname. Firstname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
            firstname = input("Enter Firstname again: \n")
        
        lastname = input("Enter Lastname: \n")
        while not self.validator.valid_lastname(lastname):
            print("Invalid lastname. Lastname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
            lastname = input("Enter Lastname again: \n")

        age = input("Enter age: \n")
        while not self.validator.check_valid_age(age):
            print("Invalid age. Age must be a number between 1 and 111.")
            age = input("Enter age: \n")


        gender = input("Enter Gender (options: male, female, other, prefer not to say): \n")
        while not self.validator.check_valid_gender(gender):
            print("Invalid gender. Please enter one of the following options: male, female, non-binary, other, prefer not to say.")
            gender = input("Enter Gender again: \n")


        weight = input("Enter Weight: \n")
        while not self.validator.check_valid_weigth(weight):
            print("Invalid weight. Weight must be a valid number.")
            weight = input("Enter Weight again: \n")

        address = self.adressform.GetAdress()

        email = input("Enter Email: \n")
        while not self.validator.check_valid_email(email) or self.services.CheckMemberEmail(email):
            email = input("Enter Email again: \n")

        mobile = "+31-6-" + input("Enter Mobile without '+316': \n")
        while not self.validator.ValidateNumber(mobile) or self.services.CheckMemberMobile(mobile):
            mobile = "+31-6-" + input("Enter Mobile again without '+316': \n")
        
        member = Member(firstname, lastname, age, gender, weight, address, email, mobile)
        print(colored('New member successfully added.', 'green'))
        print(f"Added Member: {member.firstname} {member.lastname}")
        self.utilities.SleepConsole(1.1)
        return member
        
    def SearchTermForm(self):
        search_type = input("Enter search term: \n")
        
        if search_type == '':
            print("Invalid search type.")
            self.utilities.SleepConsole(1.1)
            self.SearchTermForm()
        return search_type
    
    def SelectUserForm(self, listUser):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Found Users")
        if len(listUser) > 0:
            menuItem = 1
            for index in range(0, len(listUser)):
                if hasattr(listUser[index], 'username'):
                    print(f"{menuItem} {listUser[index].username}" )
                else:
                    print(f"{menuItem} {listUser[index].firstname} {listUser[index].lastname}" )
                menuItem +=1
            print("=================================")
            selectedOption = int(input("Select user: "))
            
            if selectedOption < menuItem:
                
                selectedIndex = selectedOption - 1
                selectedUser = listUser[selectedIndex]
                self.utilities.ClearConsole()
                self.utilities.PrintMenuTitle("Selected User")
                print( "U have selected: "  + selectedUser.firstname)
                print("=================================")
                self.utilities.SleepConsole(1.1)
                return selectedUser
            else:
                print("=====================")
                print("Wrong option! Retry!")
                self.utilities.SleepConsole(1.1)
                self.SelectUserForm(listUser)
    
    def DeleteUserForm(self, user):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Delete User")
        if hasattr(user, 'typeUser'):
            print(f"Are you sure you want to delete the {user.typeUser}: {user.username}? (y/n)")
        else:
            print(f"Are you sure you want to delete the Member: {user.firstname} {user.lastname}? (y/n)")
        confirm = input()
        if confirm.lower() == 'y':
            print("Deleting user...")
            self.utilities.SleepConsole(1.1)
            return True
        else:
            print("User deletion cancelled.")
            self.utilities.SleepConsole(1.1)
            return False
    
    def ResetConsultantForm(self, consultant):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Reset Consultant Password")
        password = input(f"Enter new Password for '{consultant.username}': \n")
        while not self.validator.valid_password(password):
            print("Invalid password. Password must be 12-30 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character.")
            password = input("Enter new Password again: \n")
        consultant.password = password
        print(f"Password Resetted!")
        self.utilities.SleepConsole(1.1)
        return consultant
    
    def ResetAdminForm(self, admin):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Reset Admin Password")
        password = input(f"Enter new Password for '{admin.username}': \n")
        while not self.validator.valid_password(password):
            print("Invalid password. Password must be 12-30 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character.")
            password = input("Enter new Password again: \n")
        admin.password = password
        print(f"Password Resetted!")
        self.utilities.SleepConsole(1.1)
        return admin
    
    def UpdateAdminForm(self, admin):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Update Admin Form")
        
        firstname = input(f"Enter Firstname (or enter to skip): \n") or admin.firstname
        while not self.validator.valid_firstname(firstname):
            print("Invalid firstname. Firstname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
            firstname = input("Enter Firstname again: \n")

        lastname = input(f"Enter Lastname (or enter to skip): \n") or admin.lastname
        while not self.validator.valid_lastname(lastname):
            print("Invalid lastname. Lastname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
            lastname = input("Enter Lastname again: \n")

        username = input(f"Enter Username (or enter to skip): \n") or admin.username
        while not self.validator.valid_username(username):
            username = input("Invalid username. Please enter a valid username: \n")

        admin.firstname = firstname
        admin.lastname = lastname
        admin.username = username

        print("Updated System Admin!")
        self.utilities.SleepConsole(1.1)
        return admin

    
    def UpdateConsultantForm(self, consultant):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Update Consultant Form")
        
        firstname = input(f"Enter Firstname (or enter to skip): \n") or consultant.firstname
        while not self.validator.valid_firstname(firstname):
             print("Invalid firstname. Firstname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
             firstname = input("Enter Firstname again: \n")
        lastname = input(f"Enter Lastname (or enter to skip): \n") or consultant.lastname
        while not self.validator.valid_lastname(lastname):
             print("Invalid lastname. Lastname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
             lastname = input("Enter Lastname again: \n")

        username = input(f"Enter Username (or enter to skip): \n") or consultant.username
        while not self.validator.valid_username(username):
            username = input("Invalid username. Please enter a valid username: \n")

        consultant.firstname = firstname
        consultant.lastname = lastname
        consultant.username = username

        print("Updated Consultant!")
        self.utilities.SleepConsole(1.1)
        return consultant

    
    def UpdateMemberForm(self, member):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Update Member Form")
        
        firstname = input(f"Enter Firstname (or enter to skip): \n") or member.firstname
        while not self.validator.valid_firstname(firstname):
             print("Invalid firstname. Firstname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
             firstname = input("Enter Firstname again: \n")
        lastname = input(f"Enter Lastname (or enter to skip): \n") or member.lastname
        while not self.validator.valid_lastname(lastname):
             print("Invalid lastname. Lastname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
             lastname = input("Enter Lastname again: \n")


        age = input(f"Enter Age (or enter to skip): \n") or member.age
        while not self.validator.check_valid_age(age):
            age = input("Invalid age. Please enter a valid age between 1 and 111: \n")

        gender = input(f"Enter Gender (or enter to skip): \n") or member.gender
        while not self.validator.check_valid_gender(gender):
            gender = input("Invalid gender. Please enter a valid gender (male, female, other, prefer not to say): \n")

        weight = input(f"Enter Weight (or enter to skip): \n") or member.weight
        while not self.validator.check_valid_weigth(weight):
            weight = input("Invalid weight. Please enter a weight between 3 and 250 kilograms: \n")

        address = self.adressform.UpdateAdress(member.adress)

        email = input(f"Enter Email (or enter to skip): \n") or member.email
        while not self.validator.check_valid_email(email):
            email = input("Invalid email. Please enter a valid email: \n")

        mobile = input(f"Enter Mobile (or enter to skip): \n") or member.mobile
        while not self.validator.ValidateNumber(mobile):
            mobile = input("Invalid mobile number. Please enter a valid mobile number: \n")

        member.firstname = firstname
        member.lastname = lastname
        member.age = int(age)
        member.gender = gender
        member.weight = float(weight)
        member.adress = address
        member.email = email
        member.mobile = mobile

        print("Updated Member!")
        self.utilities.SleepConsole(1.1)
        return member

    def UpdatePasswordForm(self):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Update Password")
        
        newPassword = input("Enter new password: \n")
        while not self.validator.valid_password(newPassword):
            newPassword = input("Invalid password. Please enter a valid password (12-30 characters long, include at least one uppercase letter, one lowercase letter, one digit, and one special character): \n")

        print("Updated Password!")
        self.utilities.SleepConsole(1.1)
        return newPassword

    
    

class AddressForm:
    validator = Validators()
    def __init__(self):
        self.cities = ["Amsterdam", "Rotterdam", "Utrecht", "Eindhoven", "Groningen", "Tilburg", "Almere", "Breda", "Nijmegen", "Haarlem"]

    def DisplayCities(self):
        print("Select a city from the list below:")
        for index, city in enumerate(self.cities, start=1):
            print(f"{index}. {city}")

    def SelectCity(self):
        while True:
            try:
                choice = int(input("Enter the number corresponding to your city: "))
                if 1 <= choice <= len(self.cities):
                    return self.cities[choice - 1]
                else:
                    print(f"Please select a number between 1 and {len(self.cities)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def GetAdress(self):
        streetname = input("Enter Street Name: ")
        while not self.validator.is_valid_street_name(streetname):
            print("Invalid street name. It should contain only letters and spaces.")
            streetname = input("Enter Street Name again: \n")
        housenumber = input("Enter House Number: ")
        while not self.validator.is_valid_housenumber(housenumber):
            print("Invalid House Number. It must be a non-negative integer.")
            housenumber = input("Enter House Number again: \n")

        while True:
            zipcode = input("Enter Zip Code (DDDDXX): ")
            if len(zipcode) == 6 and zipcode[:4].isdigit() and zipcode[4:].isalpha():
                break
            else:
                print("Invalid Zip Code format. Please enter in the format DDDDXX.")

        self.DisplayCities()
        city = self.SelectCity()

        address = f"{streetname} {housenumber}, {zipcode} {city}"
        return address
    
    def UpdateAdress(self, memberadress):
        streetname = input("Enter Street Name (or press Enter to skip): ")
        if not streetname:
            return memberadress

        housenumber = input("Enter House Number (or press Enter to skip): ")
        if not housenumber:
            return memberadress

        while True:
            zipcode = input("Enter Zip Code (DDDDXX) (or press Enter to skip): ")
            if not zipcode:
                return memberadress
            if len(zipcode) == 6 and zipcode[:4].isdigit() and zipcode[4:].isalpha():
                break
            else:
                print("Invalid Zip Code format. Please enter in the format DDDDXX.")

        self.DisplayCities()
        city = self.UpdateCity()
        if not city:
            return memberadress

        return f"{streetname} {housenumber}, {zipcode} {city}"
    
    def UpdateCity(self):
        while True:
            choice = input("Enter the number corresponding to your city (or press Enter to skip): ")
            if not choice:
                return None
            try:
                choice = int(choice)
                if 1 <= choice <= len(self.cities):
                    return self.cities[choice - 1]
                else:
                    print(f"Please select a number between 1 and {len(self.cities)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

# def main():
#     address_form = AddressForm()
#     address = address_form.get_address()
#     print("\nAddress Entered:")
#     print(f"Street Name: {address['street_name']}")
#     print(f"House Number: {address['house_number']}")
#     print(f"Zip Code: {address['zip_code']}")
#     print(f"City: {address['city']}")

# if __name__ == "__main__":
#     main()

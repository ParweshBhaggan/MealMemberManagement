

from User import Consultant, SystemAdmin, User
from Members import Member
from UserServices import UserServices
from Validation import Validators
from termcolor import colored
from Utilities import Utilities


class MenuForms:
    def __init__(self, user) -> None:
        self.loggedInUser = user
        self.validator = Validators()
        self.services = UserServices(User())
        self.utilities = Utilities()
        

    def InputOverride(self, message):
        print()
        print("Type 'back' to return to Menu ")
        message = input(f"{message}")
        if(message.lower() == "back"):
            self.Goback()     
        return message
    
    def Goback(self):
        from Menu import MenuController,MenuFunctions
        self.menu = MenuController()
        self.menu.logged_in_user = self.loggedInUser
        self.menu.menuFunctions = MenuFunctions(self.menu.logged_in_user)
        self.utilities.ClearConsole()
        self.menu.ViewMenu()
        return
    
    

    def UserForm(self, user):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("User Form")
   
       
        firstname = self.InputOverride("Enter Firstname: \n")
        while not self.validator.valid_firstname(firstname):
            print("Invalid firstname. Firstname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
            firstname =  self.InputOverride("Enter Firstname again: \n")
        
        
        lastname = self.InputOverride("Enter Lastname: \n")
        while not self.validator.valid_lastname(lastname):
            print("Invalid lastname. Lastname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
            lastname =  self.InputOverride("Enter Lastname again: \n")
        
        username = self.InputOverride("Enter Username: \n")
        while not self.validator.valid_username(username):
            print("Invalid username. Username must be 8-12 characters long and can only contain letters, digits, underscores, apostrophes, and dots.")
            username = self.InputOverride("Enter Username again: \n")

        password = self.InputOverride("Enter Password: \n")
        while not self.validator.valid_password(password):
            print("Invalid password. Password must be 12-30 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character.")
            password = self.InputOverride("Enter Password again: \n")
       
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
  
        firstname = self.InputOverride("Enter Firstname: \n")
        while not self.validator.valid_firstname(firstname):
            print("Invalid firstname. Firstname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
            firstname =  self.InputOverride("Enter Firstname again: \n")
        
        lastname = self.InputOverride("Enter Lastname: \n")
        while not self.validator.valid_lastname(lastname):
            print("Invalid lastname. Lastname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
            lastname =  self.InputOverride("Enter Lastname again: \n")

        age = self.InputOverride("Enter age: \n")
        while not self.validator.check_valid_age(age):
            print("Invalid age. Age must be a number between 1 and 111.")
            age = self.InputOverride("Enter age: \n")


        gender = self.InputOverride("Enter Gender (options: male, female, other, prefer not to say): \n")
        while not self.validator.check_valid_gender(gender):
            print("Invalid gender. Please enter one of the following options: male, female, non-binary, other, prefer not to say.")
            gender = self.InputOverride("Enter Gender again: \n")


        weight = self.InputOverride("Enter Weight: \n")
        while not self.validator.check_valid_weigth(weight):
            print("Invalid weight. Weight must be a valid number.")
            weight = self.InputOverride("Enter Weight again: \n")

        adressform = AddressForm(self.loggedInUser)
        address = adressform.GetAdress()

        email = self.InputOverride("Enter Email: \n")
        while not self.validator.check_valid_email(email) or self.services.CheckMemberEmail(email):
            email = self.InputOverride("Enter Email again: \n")

        mobile = "+31-6-" + self.InputOverride("Enter Mobile without '+316': \n")
        while not self.validator.ValidateNumber(mobile) or self.services.CheckMemberMobile(mobile):
            mobile = "+31-6-" + self.InputOverride("Enter Mobile again without '+316': \n")
        
        member = Member(firstname, lastname, age, gender, weight, address, email, mobile)
        print(colored('New member successfully added.', 'green'))
        print(f"Added Member: {member.firstname} {member.lastname}")
        self.utilities.SleepConsole(1.1)
        return member
        
    def SearchTermForm(self):
        search_type = self.InputOverride("Enter search term: \n")
        
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
            selectedOption = int(self.InputOverride("Select user: "))
            
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
        password = self.InputOverride(f"Enter new Password for '{consultant.username}': \n")
        while not self.validator.valid_password(password):
            print("Invalid password. Password must be 12-30 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character.")
            password = self.InputOverride("Enter new Password again: \n")
        consultant.password = password
        print(f"Password Resetted!")
        self.utilities.SleepConsole(1.1)
        return consultant
    
    def ResetAdminForm(self, admin):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Reset Admin Password")
        password = self.InputOverride(f"Enter new Password for '{admin.username}': \n")
        while not self.validator.valid_password(password):
            print("Invalid password. Password must be 12-30 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character.")
            password = self.InputOverride("Enter new Password again: \n")
        admin.password = password
        print(f"Password Resetted!")
        self.utilities.SleepConsole(1.1)
        return admin
    
    def UpdateAdminForm(self, admin):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Update Admin Form")
        
        firstname = self.InputOverride(f"Enter Firstname (or enter to skip): \n") or admin.firstname
        while not self.validator.valid_firstname(firstname):
            print("Invalid firstname. Firstname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
            firstname =  self.InputOverride("Enter Firstname again: \n")

        lastname = self.InputOverride(f"Enter Lastname (or enter to skip): \n") or admin.lastname
        while not self.validator.valid_lastname(lastname):
            print("Invalid lastname. Lastname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
            lastname =  self.InputOverride("Enter Lastname again: \n")

        username = self.InputOverride(f"Enter Username (or enter to skip): \n") or admin.username
        while not self.validator.valid_username(username):
            username =  self.InputOverride("Invalid username. Please enter a valid username: \n")

        admin.firstname = firstname
        admin.lastname = lastname
        admin.username = username

        print("Updated System Admin!")
        self.utilities.SleepConsole(1.1)
        return admin

    
    def UpdateConsultantForm(self, consultant):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Update Consultant Form")
        
        firstname = self.InputOverride(f"Enter Firstname (or enter to skip): \n") or consultant.firstname
        while not self.validator.valid_firstname(firstname):
             print("Invalid firstname. Firstname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
             firstname =  self.InputOverride("Enter Firstname again: \n")
        lastname = self.InputOverride(f"Enter Lastname (or enter to skip): \n") or consultant.lastname
        while not self.validator.valid_lastname(lastname):
             print("Invalid lastname. Lastname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
             lastname =  self.InputOverride("Enter Lastname again: \n")

        username = self.InputOverride(f"Enter Username (or enter to skip): \n") or consultant.username
        while not self.validator.valid_username(username):
            username =  self.InputOverride("Invalid username. Please enter a valid username: \n")

        consultant.firstname = firstname
        consultant.lastname = lastname
        consultant.username = username

        print("Updated Consultant!")
        self.utilities.SleepConsole(1.1)
        return consultant

    
    def UpdateMemberForm(self, member):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Update Member Form")
        
        firstname = self.InputOverride(f"Enter Firstname (or enter to skip): \n") or member.firstname
        while not self.validator.valid_firstname(firstname):
             print("Invalid firstname. Firstname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
             firstname =  self.InputOverride("Enter Firstname again: \n")
        lastname = self.InputOverride(f"Enter Lastname (or enter to skip): \n") or member.lastname
        while not self.validator.valid_lastname(lastname):
             print("Invalid lastname. Lastname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
             lastname =  self.InputOverride("Enter Lastname again: \n")


        age = self.InputOverride(f"Enter Age (or enter to skip): \n") or member.age
        while not self.validator.check_valid_age(age):
            age =  self.InputOverride("Invalid age. Please enter a valid age between 1 and 111: \n")

        gender = self.InputOverride(f"Enter Gender (or enter to skip): \n") or member.gender
        while not self.validator.check_valid_gender(gender):
            gender =  self.InputOverride("Invalid gender. Please enter a valid gender (male, female, other, prefer not to say): \n")

        weight = self.InputOverride(f"Enter Weight (or enter to skip): \n") or member.weight
        while not self.validator.check_valid_weigth(weight):
            weight =  self.InputOverride("Invalid weight. Please enter a weight between 3 and 250 kilograms: \n")

        addressform = AddressForm(self.loggedInUser)
        adress = addressform.UpdateAdress(member.adress)

        email = self.InputOverride(f"Enter Email (or enter to skip): \n") or member.email
        while not self.validator.check_valid_email(email):
            email = self.InputOverride("Invalid email. Please enter a valid email: \n")

        mobile = self.InputOverride(f"Enter Mobile (or enter to skip): \n") or member.mobile
        while not self.validator.ValidateNumber(mobile):
            mobile = self.InputOverride("Invalid mobile number. Please enter a valid mobile number: \n")

        member.firstname = firstname
        member.lastname = lastname
        member.age = int(age)
        member.gender = gender
        member.weight = float(weight)
        member.adress = adress
        member.email = email
        member.mobile = mobile

        print("Updated Member!")
        self.utilities.SleepConsole(1.1)
        return member

    def UpdatePasswordForm(self):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Update Password")
        
        newPassword = self.InputOverride("Enter new password: \n")
        while not self.validator.valid_password(newPassword):
            print("Invalid password. Password must be 12-30 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character.")
            newPassword =  self.InputOverride("Invalid password. Please enter a valid password (12-30 characters long, include at least one uppercase letter, one lowercase letter, one digit, and one special character): \n")

        print("Updated Password!")
        self.utilities.SleepConsole(1.1)
        return newPassword

    
    

class AddressForm:
    validator = Validators()
    def __init__(self, user):
        self.form = MenuForms(user)
        self.cities = ["Amsterdam", "Rotterdam", "Utrecht", "Eindhoven", "Groningen", "Tilburg", "Almere", "Breda", "Nijmegen", "Haarlem"]

    def DisplayCities(self):
        print("Select a city from the list below:")
        for index, city in enumerate(self.cities, start=1):
            print(f"{index}. {city}")

    def SelectCity(self):
        while True:
            try:
                choice = int(self.form.InputOverride("Enter the number corresponding to your city: "))
                if 1 <= choice <= len(self.cities):
                    return self.cities[choice - 1]
                else:
                    print(f"Please select a number between 1 and {len(self.cities)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def GetAdress(self):
        streetname = self.form.InputOverride("Enter Street Name: ")
        while not self.validator.is_valid_street_name(streetname):
            print("Invalid street name. It should contain only letters and spaces.")
            streetname = self.form.InputOverride("Enter Street Name again: \n")
        housenumber = self.form.InputOverride("Enter House Number: ")
        while not self.validator.is_valid_housenumber(housenumber):
            print("Invalid House Number. It must be a non-negative integer.")
            housenumber = self.form.InputOverride("Enter House Number again: \n")

        while True:
            zipcode = self.form.InputOverride("Enter Zip Code (DDDDXX): ")
            if len(zipcode) == 6 and zipcode[:4].isdigit() and zipcode[4:].isalpha():
                zipcode = zipcode.upper()
                break
            else:
                print("Invalid Zip Code format. Please enter in the format DDDDXX.")

        self.DisplayCities()
        city = self.SelectCity()

        address = f"{streetname} {housenumber}, {zipcode} {city}"
        return address
    
    def UpdateAdress(self, memberadress):
        streetname = self.form.InputOverride("Enter Street Name (or press Enter to skip): ")
        if not streetname:
            return memberadress

        housenumber = self.form.InputOverride("Enter House Number (or press Enter to skip): ")
        if not housenumber:
            return memberadress

        while True:
            zipcode = self.form.InputOverride("Enter Zip Code (DDDDXX) (or press Enter to skip): ")
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
            choice = self.form.InputOverride("Enter the number corresponding to your city (or press Enter to skip): ")
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


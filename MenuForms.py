from datetime import datetime
import os
from Logger import log
from User import Consultant, SystemAdmin, User
from Members import Member
from UserServices import UserServices
from Validation import Validators
from termcolor import colored
from Utilities import Utilities


class MenuForms:
    '''This class handles the functions of different type of forms'''
    def __init__(self, user) -> None:
        self.loggedInUser = user
        self.validator = Validators()
        self.services = UserServices(User())
        self.utilities = Utilities()
        

    def InputOverride(self, message):
        '''Is an override function for standard input() function'''
        print()
        print(self.utilities.ReturnMessage("Type 'back' to return to Menu"))
        message = self.utilities.ConsoleMessage(message)
        try:
            message = input(f"{message}")
        except KeyboardInterrupt:
            print(self.utilities.ErrorMessage("Invalid key!"))
            return self.InputOverride(message)
        if(message.lower() == "back"):
            print(self.utilities.ConsoleMessage("Returning to Menu..."))
            self.utilities.SleepConsole(1.1)
            self.ReturnToHome()     
        return message
    
    def ReturnToHome(self):
        '''Function that navigates back to the home menu'''
        from Menu import MenuController,MenuFunctions
        self.menu = MenuController()
        self.menu.logged_in_user = self.loggedInUser
        self.menu.menuFunctions = MenuFunctions(self.menu.logged_in_user)
        self.utilities.ClearConsole()
        self.menu.ViewMenu()
        return

    def UserForm(self, user):
        '''The form for creating a new User'''
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("User Form")

        log(self.loggedInUser.username, "Opening User Form", "UserForm")

        firstname = self.InputOverride("Enter Firstname: \n")
        while not self.validator.valid_firstname(firstname):
            log(self.loggedInUser.username, "Input validation failure: Invalid firstname entered", "InputValidationFailure")
            print("Invalid firstname. Firstname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
            firstname = self.InputOverride("Enter Firstname again: \n")

        lastname = self.InputOverride("Enter Lastname: \n")
        while not self.validator.valid_lastname(lastname):
            log(self.loggedInUser.username, "Input validation failure: Invalid lastname entered", "InputValidationFailure")
            print("Invalid lastname. Lastname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
            lastname = self.InputOverride("Enter Lastname again: \n")

        name = user.__class__.__name__
        username = self.InputOverride("Enter Username: \n")
        while not self.validator.valid_username(username) or self.services.CheckUsername(name, username):
            log(self.loggedInUser.username, "Input validation failure: Invalid or duplicate username entered", "InputValidationFailure")
            print("Invalid username. Username must be 8-12 characters long and can only contain letters, digits, underscores, apostrophes, and dots.")
            username = self.InputOverride("Enter Username again: \n")

        password = self.InputOverride("Enter Password: \n")
        while not self.validator.valid_password(password):
            log(self.loggedInUser.username, "Input validation failure: Invalid password entered", "InputValidationFailure")
            print("Invalid password. Password must be 12-30 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character.")
            password = self.InputOverride("Enter Password again: \n")

        # Creating the user object based on its type
        if name == "SystemAdmin":
            user = SystemAdmin(firstname, lastname, username, password)
        elif name == "Consultant":
            user = Consultant(firstname, lastname, username, password)

        print(f"Added User: {user.firstname} {user.lastname} {user.typeUser}")
        self.utilities.SleepConsole(1.1)
        return user


    def MemberForm(self):
        '''The form for creating a new Member'''

        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Member Form")

        log(self.loggedInUser.username, "Opening Member Form", "MemberForm")

        firstname = self.InputOverride("Enter Firstname: \n")
        while not self.validator.valid_firstname(firstname):
            log(self.loggedInUser.username, "Input validation failure: Invalid firstname entered", "InputValidationFailure")
            print("Invalid firstname. Firstname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
            firstname = self.InputOverride("Enter Firstname again: \n")

        lastname = self.InputOverride("Enter Lastname: \n")
        while not self.validator.valid_lastname(lastname):
            log(self.loggedInUser.username, "Input validation failure: Invalid lastname entered", "InputValidationFailure")
            print("Invalid lastname. Lastname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
            lastname = self.InputOverride("Enter Lastname again: \n")

        age = self.InputOverride("Enter Age: \n")
        while not self.validator.check_valid_age(age):
            log(self.loggedInUser.username, "Input validation failure: Invalid age entered", "InputValidationFailure")
            print("Invalid age. Age must be a number between 1 and 111.")
            age = self.InputOverride("Enter Age: \n")

        gender = self.SelectGender()

        weight = self.InputOverride("Enter Weight: \n")
        while not self.validator.check_valid_weigth(weight):
            log(self.loggedInUser.username, "Input validation failure: Invalid weight entered", "InputValidationFailure")
            print("Invalid weight. Weight must be a valid number.")
            weight = self.InputOverride("Enter Weight again: \n")

        adressform = AddressForm(self.loggedInUser)
        address = adressform.GetAdress()

        email = self.InputOverride("Enter Email: \n")
        while not self.validator.check_valid_email(email) or self.services.CheckMemberEmail(email):
            log(self.loggedInUser.username, "Input validation failure: Invalid or duplicate email entered", "InputValidationFailure")
            email = self.InputOverride("Enter Email again: \n")

        mobile = "+31-6-" + self.InputOverride("Enter Mobile without '+316': \n")
        while not self.validator.ValidateNumber(mobile) or self.services.CheckMemberMobile(mobile):
            log(self.loggedInUser.username, "Input validation failure: Invalid or duplicate mobile number entered", "InputValidationFailure")
            mobile = "+31-6-" + self.InputOverride("Enter Mobile again without '+316': \n")
        
        # Creating the Member object
        member = Member(firstname, lastname, age, gender, weight, address, email, mobile)

        print(colored('New Member successfully added.', 'green'))
        print(f"Added Member: {member.firstname} {member.lastname}")
        self.utilities.SleepConsole(1.1)
        return member

        
    def SearchTermForm(self):
        '''The form for searching Users/Members'''
        search_type = self.InputOverride("Enter search term: \n")
        
        if search_type == '':
            print("Invalid search type.")
            self.utilities.SleepConsole(1.1)
            return self.SearchTermForm()
        return search_type
    
    def SelectUserForm(self, listUser):
        '''The form for selecting specific found Users/Members'''
        self.utilities.ClearConsole()
        isUser = False
        
        if len(listUser) > 0:
            menuItem = 1
            #if listUser has user
            if hasattr(listUser[0], 'username'):
                isUser = True
                self.utilities.PrintMenuTitle("Found Users")
                optionMsg = self.utilities.ConsoleMessage("Option")
                usernMsg = self.utilities.SuccessMessage("Username")
                typeMsg = self.utilities.ErrorMessage("Type")
                print(f"{optionMsg}  |   {usernMsg}    |   {typeMsg}")
            
            #if listUser has Member
            else:
                self.utilities.PrintMenuTitle("Found Members")
                optionMsg = self.utilities.ConsoleMessage("Option")
                usernMsg = self.utilities.SuccessMessage("FirstName")
                typeMsg = self.utilities.ErrorMessage("LastName")
                print(f"{optionMsg}  |   {usernMsg}    |   {typeMsg}")
            
            
            for index in range(0, len(listUser)):
                
                #display each User in list
                if hasattr(listUser[index], 'username'):
                    optionMsg = self.utilities.ConsoleMessage(menuItem)
                    usernMsg = self.utilities.SuccessMessage(listUser[index].username)
                    typeMsg = self.utilities.ErrorMessage(listUser[index].typeUser)
                    print(f"{optionMsg}  |   {usernMsg}, {typeMsg}" )
                
                #display each Member in list
                else:
                    optionMsg = self.utilities.ConsoleMessage(menuItem)
                    usernMsg = self.utilities.SuccessMessage(listUser[index].firstname)
                    typeMsg = self.utilities.ErrorMessage(listUser[index].lastname)
                    print(f"{optionMsg}  |   {usernMsg}, {typeMsg}" )
                menuItem +=1
            print("=================================")
            while True:

                #prompt the selection
                if(isUser):
                    selectedOption = self.InputOverride("Select User: \n")
                else:
                    selectedOption = self.InputOverride("Select Member: \n")
                if not selectedOption:
                    return None
                
                #handle selection errors
                try:
                    selectedOption = int(selectedOption)
                    if 1 <= selectedOption <= len(listUser):
                        break
                    else:
                        mess = self.utilities.ConsoleMessage(f"Please select a number between 1 and {len(listUser)}.")
                        print(mess)
                except ValueError:
                    errormsg = self.utilities.ErrorMessage("Invalid input. Please enter a number.")
                    print(errormsg)

            #if selected
            if selectedOption < menuItem:
                
                selectedIndex = selectedOption - 1
                selectedUser = listUser[selectedIndex]
                self.utilities.ClearConsole()
                if(isUser):
                    self.utilities.PrintMenuTitle("Selected User")
                    usernMsg = self.utilities.SuccessMessage(selectedUser.username)
                    typeMsg = self.utilities.ErrorMessage(selectedUser.typeUser)
                    print(f"U have selected: {usernMsg} {typeMsg}" )
                    log(self.loggedInUser.username, "Selected user.", f"User: {selectedUser.username}")
                else:
                    self.utilities.PrintMenuTitle("Selected Member")
                    usernMsg = self.utilities.SuccessMessage(selectedUser.firstname)
                    typeMsg = self.utilities.ErrorMessage(selectedUser.lastname)
                    print(f"U have selected: {usernMsg} {typeMsg}" )
                    log(self.loggedInUser.username, "Selected member.", f"Member: {selectedUser.firstname} {selectedUser.lastname}")
                print("=================================")
                self.utilities.SleepConsole(1.1)
                return selectedUser
            else:
                print("=====================")
                print("Wrong option! Retry!")
                self.utilities.SleepConsole(1.1)
                self.SelectUserForm(listUser)

    
    def DeleteUserForm(self, user):
        '''The form for deleting a user'''
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Delete User")
        if hasattr(user, 'typeUser'):
            print(f"Are you sure you want to delete {user.typeUser}: {user.username}? (y/n)")
        else:
            print(f"Are you sure you want to delete Member: {user.firstname} {user.lastname}? (y/n)")
        confirm = input()
        if confirm.lower() == 'y':
            print("Deleting User...")
            self.utilities.SleepConsole(1.1)
            return True
        else:
            print("User deletion cancelled.")
            self.utilities.SleepConsole(1.1)
            return False
        
    
    def ResetConsultantForm(self, consultant):
        '''The form for password resetting a Consultant'''
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Reset Consultant Password")
        password = self.InputOverride(f"Enter new Password for '{consultant.username}': \n")
        while not self.validator.valid_password(password):
            log(self.loggedInUser.username, "Input validation failure: Invalid password entered", "InputValidationFailure")
            print("Invalid password. Password must be 12-30 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character.")
            password = self.InputOverride("Enter new Password again: \n")
        consultant.password = password
        print(f"Password Resetted!")
        self.utilities.SleepConsole(1.1)
        return consultant
    
    def ResetAdminForm(self, admin):
        '''The form for password resetting a System Admin'''
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Reset Admin Password")
        password = self.InputOverride(f"Enter new Password for '{admin.username}': \n")
        while not self.validator.valid_password(password):
            log(self.loggedInUser.username, "Input validation failure: Invalid password entered", "InputValidationFailure")
            print("Invalid password. Password must be 12-30 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character.")
            password = self.InputOverride("Enter new Password again: \n")
        admin.password = password
        print(f"Password Resetted!")
        self.utilities.SleepConsole(1.1)
        return admin
    
    def UpdateAdminForm(self, admin):
        '''The form for updating a System Admin'''
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Update Admin Form")
        
        firstname = self.InputOverride(f"Enter Firstname (or enter to skip): \n") or admin.firstname
        while not self.validator.valid_firstname(firstname):
            log(self.loggedInUser.username, "Input validation failure: Invalid firstname entered", "InputValidationFailure")
            print("Invalid firstname. Firstname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
            firstname =  self.InputOverride("Enter Firstname again: \n")

        lastname = self.InputOverride(f"Enter Lastname (or enter to skip): \n") or admin.lastname
        while not self.validator.valid_lastname(lastname):
            log(self.loggedInUser.username, "Input validation failure: Invalid lastname entered", "InputValidationFailure")
            print("Invalid lastname. Lastname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
            lastname =  self.InputOverride("Enter Lastname again: \n")

        username = self.InputOverride(f"Enter Username (or enter to skip): \n") or admin.username
        while not self.validator.valid_username(username) or (username != admin.username and self.services.CheckUsername(admin.typeUser, username)):
            log(self.loggedInUser.username, "Input validation failure: Invalid username entered", "InputValidationFailure")
            username =  self.InputOverride("Invalid username. Please enter a valid username: \n")

        admin.firstname = firstname
        admin.lastname = lastname
        admin.username = username

        print("Updated System Admin!")
        self.utilities.SleepConsole(1.1)
        return admin

    
    def UpdateConsultantForm(self, consultant):
        '''The form for updating a Consultant'''
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Update Consultant Form")
        
        firstname = self.InputOverride(f"Enter Firstname (or enter to skip): \n") or consultant.firstname
        while not self.validator.valid_firstname(firstname):
            log(self.loggedInUser.username, "Input validation failure: Invalid firstname entered", "InputValidationFailure")
            print("Invalid firstname. Firstname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
            firstname =  self.InputOverride("Enter Firstname again: \n")
        
        lastname = self.InputOverride(f"Enter Lastname (or enter to skip): \n") or consultant.lastname
        while not self.validator.valid_lastname(lastname):
            log(self.loggedInUser.username, "Input validation failure: Invalid lastname entered", "InputValidationFailure")
            print("Invalid lastname. Lastname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
            lastname =  self.InputOverride("Enter Lastname again: \n")

        username = self.InputOverride(f"Enter Username (or enter to skip): \n") or consultant.username
        while not self.validator.valid_username(username) or (username != consultant.username and self.services.CheckUsername(consultant.typeUser, username)):
            log(self.loggedInUser.username, "Input validation failure: Invalid username entered", "InputValidationFailure")
            username =  self.InputOverride("Invalid username. Please enter a valid username: \n")

        consultant.firstname = firstname
        consultant.lastname = lastname
        consultant.username = username

        print("Updated Consultant!")
        self.utilities.SleepConsole(1.1)
        return consultant



    def SelectGender(self):
        '''Handles the selection of gender section'''
        print("\nGender:\n")
        gender_options=['Male', 'Female', 'Other', 'Prefer Not To Say']
        index = 1
        for item in gender_options:
            print(f'{str(index)} {item}')
            index+=1
        
        choice = self.InputOverride("Select gender: ")
        try:
            choice = int(choice)
        except ValueError:
            log(self.loggedInUser.username, "Input validation failure: Invalid gender key entered", "InputValidationFailure")
            print(self.utilities.ErrorMessage("Invalid Key!"))
            return self.SelectGender()
        else:
            if(choice > len(gender_options) or choice < 0):
                log(self.loggedInUser.username, "Input validation failure: Invalid gender choice entered", "InputValidationFailure")
                print(self.utilities.ConsoleMessage("Invalid Option!"))
                return self.SelectGender()
            else:        
                gender = gender_options[choice - 1]
                print("selected gender: " + gender)
                return gender
    
    def UpdateMemberForm(self, member):
        '''The form for updating a Member'''
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Update Member Form")
        
        firstname = self.InputOverride(f"Enter Firstname (or enter to skip): \n") or member.firstname
        while not self.validator.valid_firstname(firstname):
            log(self.loggedInUser.username, "Input validation failure: Invalid firstname entered", "InputValidationFailure")
            print("Invalid firstname. Firstname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
            firstname =  self.InputOverride("Enter Firstname again: \n") or member.firstname
        
        lastname = self.InputOverride(f"Enter Lastname (or enter to skip): \n") or member.lastname
        while not self.validator.valid_lastname(lastname):
            log(self.loggedInUser.username, "Input validation failure: Invalid lastname entered", "InputValidationFailure")
            print("Invalid lastname. Lastname must be between 2 and 30 characters and can only contain letters, spaces, hyphens, and apostrophes.")
            lastname =  self.InputOverride("Enter Lastname again: \n") or member.lastname

        age = self.InputOverride(f"Enter Age (or enter to skip): \n") or member.age
        while not self.validator.check_valid_age(age):
            log(self.loggedInUser.username, "Input validation failure: Invalid age entered", "InputValidationFailure")
            age =  self.InputOverride("Invalid age. Please enter a valid age between 1 and 111: \n") or member.age

        gender = self.SelectGender()

        weight = self.InputOverride(f"Enter Weight (or enter to skip): \n") or member.weight
        while not self.validator.check_valid_weigth(weight):
            log(self.loggedInUser.username, "Input validation failure: Invalid weight entered", "InputValidationFailure")
            weight =  self.InputOverride("Invalid weight. Please enter a weight between 3 and 250 kilograms: \n") or member.weight

        addressform = AddressForm(self.loggedInUser)
        adress = addressform.UpdateAdress(member.adress)

        email = self.InputOverride(f"Enter Email (or enter to skip): \n") or member.email
        while not self.validator.check_valid_email(email) or (str(member.email).lower() != email.lower() and self.services.CheckMemberEmail(email)):
            log(self.loggedInUser.username, "Input validation failure: Invalid email entered", "InputValidationFailure")
            email = self.InputOverride("Invalid email. Please enter a valid email: \n") or member.email

        mobile = self.InputOverride(f"Enter Mobile (or enter to skip): \n") or member.mobile
        if len(mobile) == 8:
            mobile = "+31-6-" + mobile
        while not self.validator.ValidateNumber(mobile) or (mobile != member.mobile and self.services.CheckMemberMobile(mobile)):
            log(self.loggedInUser.username, "Input validation failure: Invalid mobile number entered", "InputValidationFailure")
            mobile = self.InputOverride("Invalid mobile number. Please enter a valid mobile number: \n") or member.mobile
            if len(mobile) == 8:
                mobile = "+31-6-" + mobile

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
        '''The form for updating a Password of a user'''
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Update Password")
        
        newPassword = self.InputOverride("Enter new password: \n")
        while not self.validator.valid_password(newPassword):
            log(self.loggedInUser.username, "Input validation failure: Invalid password entered", "InputValidationFailure")
            print("Invalid password. Password must be 12-30 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character.")
            newPassword =  self.InputOverride("Invalid password. Please enter a valid password (12-30 characters long, include at least one uppercase letter, one lowercase letter, one digit, and one special character): \n")
        
        confirmPassword = self.InputOverride("Confirm new password: \n")
        while newPassword != confirmPassword:
            log(self.loggedInUser.username, "Input validation failure: Passwords do not match", "InputValidationFailure")
            print("Passwords do not match. Please try again.")
            newPassword = self.InputOverride("Enter new password: \n")
            while not self.validator.valid_password(newPassword):
                log(self.loggedInUser.username, "Input validation failure: Invalid password entered", "InputValidationFailure")
                print("Invalid password. Password must be 12-30 characters long and include at least one uppercase letter, one lowercase letter, one digit, and one special character.")
                newPassword =  self.InputOverride("Invalid password. Please enter a valid password (12-30 characters long, include at least one uppercase letter, one lowercase letter, one digit, and one special character): \n")
            
            confirmPassword = self.InputOverride("Confirm new password: \n")

        print("Password successfully updated.")
        self.utilities.SleepConsole(1.5)
        return newPassword

    
    def PrintMemberForm(self, member):
        '''Displays a Member in the console'''
        if member is not None:
            print("Membership ID: " + str(member.membershipID))
            print("Firstname: " + member.firstname)
            print("Lastname: " + member.lastname)
            print("Age: " + str(member.age))
            print("Gender: " + member.gender)
            print("Email: " + member.email)
            print("Adress: " + member.adress)
            print("Weight: " + str(member.weight))
            print("Mobile: " + member.mobile)
            print("Registration date: " + str(member.registrationdate))
            # input("Press (enter) key to go back")
            return
        print("No member found or selected!\nReturning...")
        return

    def PrintUserForm(self, user):
        '''Displays a User in the console'''
        if user is not None:
            print("Firstname: " + user.firstname)
            print("Lastname: " + user.lastname)
            print("Username: " + user.username)
            #print("Password: " + user.password)
            print("Registration date: " + str(user.registrationdate))
            print("TypeUser: " + user.typeUser)
            # input("Press (enter) key to go back")
            return
        print("No User found\nGoing back..............")
        return
    
    def UpdateOrDeleteForm(self, *args):
        '''The form after selecting a user or member'''
        print("\n===================Updating or Deleting===================")
        user = None
        menu_items = None
        if(len(args) > 0):
            user = args[0]
        if user.__class__.__name__ == "Member" and self.loggedInUser.typeUser == "Consultant":
            menu_items = [
                "Update Member"
            ]
        elif user.__class__.__name__ == "Member":
            menu_items = [
                "Update Member",
                "Delete Member"
            ]
        else:
            menu_items = [
                "Update User",
                "Delete User",
                "Reset Password User"
            ]
        
        index = 1
        for item in menu_items:
            print(f"{str(index)} {item}")
            index+=1

        while True:
            try:
                choice = int(self.InputOverride("Select Option: \n"))
                if 1 <= choice <= len(menu_items):
                    return choice
                else:
                    log(self.loggedInUser.username, "Input validation failure: Invalid number entered", "InputValidationFailure")
                    mess = self.utilities.ConsoleMessage(f"Please select a number corresponding with the options given.")
                    print(mess)
            except ValueError:
                log(self.loggedInUser.username, "Input validation failure: Invalid input entered", "InputValidationFailure")
                mess = self.utilities.ErrorMessage("Invalid input. Please enter a number.")
                print(mess)

    def CreateBackupForm(self):
        '''The form for creating a back up'''
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Creating Backup")
        print("1 Create a backup")
        while True:
            try:
                choice = int(self.InputOverride("Select Option: \n"))
                if choice == 1:
                    print("Are you sure you want to create a backup? (y/n)")
                    confirm = input()
                    if confirm.lower() == 'y':
                        print("Creating Backup...")
                        self.utilities.SleepConsole(1.1)
                        return True
                    else:
                        print("Backup creation cancelled.")
                        self.utilities.SleepConsole(1.1)
                        return False
                else:
                    log(self.loggedInUser.username, "Input validation failure: Invalid option selected", "InputValidationFailure")
                    mess = self.utilities.ConsoleMessage("Please select number 1 to make backup")
                    print(mess)
            except ValueError:
                log(self.loggedInUser.username, "Input validation failure: Invalid input entered", "InputValidationFailure")
                mess = self.utilities.ErrorMessage("Invalid input. Please enter a number.")
                print(mess)

    def RetrieveBackupForm(self):
        '''The form for retrieving a back up'''
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Retrieve Backup")
        print("Are you sure you want to retrieve the backup? (y/n)")
        confirm = input()
        if confirm.lower() == 'y':
            print("Restoring...")
            self.utilities.SleepConsole(1.1)
            return True
        else:
            print("Restore backup cancelled.")
            self.utilities.SleepConsole(1.1)
            return False

    def DisplayAndSelectBackups(self, backups):
        '''The form for that displays multiple existing back up data'''
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Restore Backup")
        print("Select a backup from the list below:")
        for index, backup in enumerate(backups, start=1):
            backup_path = os.path.join("Backupfolder", backup)
            creation_time = datetime.fromtimestamp(os.path.getctime(backup_path)).strftime('%H:%M:%S')
            print(f"{index}. {backup} - Created: {creation_time}")

        while True:
            try:
                choice = int(self.InputOverride("Enter the number corresponding to your backup: \n"))
                if 1 <= choice <= len(backups):
                    return backups[choice - 1]
                else:
                    log(self.loggedInUser.username, "Input validation failure: Invalid backup selection", "InputValidationFailure")
                    print(f"Please select a number between 1 and {len(backups)}.")
            except ValueError:
                log(self.loggedInUser.username, "Input validation failure: Invalid input entered", "InputValidationFailure")
                print("Invalid input. Please enter a number.")
    

class AddressForm:
    '''This class handles how the adress section functions'''
    validator = Validators()
    def __init__(self, user):
        self.user = user
        self.form = MenuForms(user)
        self.cities = ["Amsterdam", "Rotterdam", "Utrecht", "Eindhoven", "Groningen", "Tilburg", "Almere", "Breda", "Nijmegen", "Haarlem"]

    def DisplayCities(self):
        '''Displays selection of cities'''
        print("Select a city from the list below:")
        for index, city in enumerate(self.cities, start=1):
            print(f"{index}. {city}")

    def SelectCity(self):
        '''Returns selected city'''
        while True:
            try:
                choice = int(self.form.InputOverride("Enter the number corresponding to your city: "))
                if 1 <= choice <= len(self.cities):
                    return self.cities[choice - 1]
                else:
                    print(f"Please select a number between 1 and {len(self.cities)}.")
                    log(self.user.username, "Input validation failure: Invalid city selection", "InputValidationFailure")
            except ValueError:
                print("Invalid input. Please enter a number.")
                log(self.user.username, "Input validation failure: Invalid input entered", "InputValidationFailure")

    def GetAdress(self):
        '''Handles entering the adress'''
        streetname = self.form.InputOverride("Enter Street Name: \n")
        while not self.validator.is_valid_street_name(streetname):
            print("Invalid street name. It should contain only letters and spaces.")
            log(self.user.username, "Input validation failure: Invalid street name entered", "InputValidationFailure")
            streetname = self.form.InputOverride("Enter Street Name again: \n")

        housenumber = self.form.InputOverride("Enter House Number: \n")
        while not self.validator.is_valid_housenumber(housenumber):
            print("Invalid House Number. It must be a non-negative integer.")
            log(self.user.username, "Input validation failure: Invalid house number entered", "InputValidationFailure")
            housenumber = self.form.InputOverride("Enter House Number again: \n")

        while True:
            zipcode = self.form.InputOverride("Enter Zip Code (DDDDXX): \n")
            if len(zipcode) == 6 and zipcode[:4].isdigit() and zipcode[4:].isalpha():
                zipcode = zipcode.upper()
                break
            else:
                print("Invalid Zip Code format. Please enter in the format DDDDXX.")
                log(self.user.username, "Input validation failure: Invalid zip code entered", "InputValidationFailure")

        self.DisplayCities()
        city = self.SelectCity()

        address = f"{streetname} {housenumber}, {zipcode} {city}"
        return address
    
    def UpdateAdress(self, memberadress):
        '''Handles updating the adress'''
        streetname = self.form.InputOverride("Enter Street Name (or press Enter to skip): \n")
        if not streetname:
            return memberadress
        while not self.validator.is_valid_street_name(streetname):
            print("Invalid street name. It should contain only letters and spaces.")
            log(self.user.username, "Input validation failure: Invalid street name entered", "InputValidationFailure")
            streetname = self.form.InputOverride("Enter Street Name again (or press Enter to skip): \n")
            if not streetname:
                return memberadress

        housenumber = self.form.InputOverride("Enter House Number (or press Enter to skip): \n")
        if not housenumber:
            return memberadress
        while not self.validator.is_valid_housenumber(housenumber):
            print("Invalid House Number. It must be a non-negative integer.")
            log(self.user.username, "Input validation failure: Invalid house number entered", "InputValidationFailure")
            housenumber = self.form.InputOverride("Enter House Number again (or press Enter to skip): \n")
            if not housenumber:
                return memberadress

        while True:
            zipcode = self.form.InputOverride("Enter Zip Code (DDDDXX) (or press Enter to skip): \n")
            if not zipcode:
                return memberadress
            if len(zipcode) == 6 and zipcode[:4].isdigit() and zipcode[4:].isalpha():
                break
            else:
                print("Invalid Zip Code format. Please enter in the format DDDDXX.")
                log(self.user.username, "Input validation failure: Invalid zip code entered", "InputValidationFailure")

        self.DisplayCities()
        city = self.UpdateCity()
        if not city:
            return memberadress
        return f"{streetname} {housenumber}, {zipcode} {city}"
    
    def UpdateCity(self):
        '''Handles updating the city'''
        while True:
            choice = self.form.InputOverride("Enter the number corresponding to your city (or press Enter to skip): \n")
            if not choice:
                return None
            try:
                choice = int(choice)
                if 1 <= choice <= len(self.cities):
                    return self.cities[choice - 1]
                else:
                    print(f"Please select a number between 1 and {len(self.cities)}.")
                    log(self.user.username, "Input validation failure: Invalid city selection", "InputValidationFailure")
            except ValueError:
                print("Invalid input. Please enter a number.")
                log(self.user.username, "Input validation failure: Invalid input entered", "InputValidationFailure")

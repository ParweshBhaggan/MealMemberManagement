
from User import Consultant, SuperAdmin, SystemAdmin
from Members import Member
from Utilities import Utilities


class MenuForms:
    def __init__(self):
        self.utilities = Utilities()
        

    def UserForm(self, user):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("User Form")
        firstname = input("Enter Firstname: \n")
        lastname = input("Enter Lastname: \n")
        username = input("Enter Username: \n")
        password = input("Enter Password: \n")
        
        name = user.__class__.__name__
        if(name == "SystemAdmin"):
            user = SystemAdmin(firstname, lastname, username, password)
        elif(name == "Consultant"):
            user = Consultant(firstname, lastname, username, password)
        return user

    def MemberForm(self):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Member Form")
        firstname = input("Enter Firstname: \n")
        lastname = input("Enter Lastname: \n")
        age = int(input("Enter Age: \n"))
        gender = input("Enter Gender: \n")
        weight = float(input("Enter Weight: \n"))
        address = input("Enter Address: \n")
        email = input("Enter Email: \n")
        mobile = input("Enter Mobile: \n")

        member = Member(firstname, lastname, age, gender, weight, address, email, mobile)
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
        consultant.password = password
        return consultant
    
    def ResetAdminForm(self, admin):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Reset Admin Password")
        password = input(f"Enter new Password for '{admin.username}': \n")
        admin.password = password
        return admin
    
    def UpdateAdminForm(self, admin):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Update Admin Form")
        firstname = input(f"Enter Firstname (or enter to skip): \n") or admin.firstname
        lastname = input(f"Enter Lastname (or enter to skip): \n") or admin.lastname
        username = input(f"Enter Username (or enter to skip): \n") or admin.username

        admin.firstname = firstname
        admin.lastname = lastname
        admin.username = username
        admin.password = admin.password

        return admin
    
    def UpdateConsultantForm(self, consultant):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Update Consultant Form")
        firstname = input(f"Enter Firstname (or enter to skip): \n") or consultant.firstname
        lastname = input(f"Enter Lastname (or enter to skip): \n") or consultant.lastname
        username = input(f"Enter Username (or enter to skip): \n") or consultant.username

        consultant.firstname = firstname
        consultant.lastname = lastname
        consultant.username = username
        consultant.password = consultant.password

        return consultant
    
    def UpdateMemberForm(self, member):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Update Member Form")
        firstname = input(f"Enter Firstname (or enter to skip): \n") or member.firstname
        lastname = input(f"Enter Lastname (or enter to skip): \n") or member.lastname
        age = input(f"Enter Age (or enter to skip): \n") or member.age
        gender = input(f"Enter Gender (or enter to skip): \n") or member.gender
        weight = input(f"Enter Weight (or enter to skip): \n") or member.weight
        adress = input(f"Enter Address (or enter to skip): \n") or member.adress
        email = input(f"Enter Email (or enter to skip): \n") or member.email
        mobile = input(f"Enter Mobile (or enter to skip): \n") or member.mobile

        member.firstname = firstname
        member.lastname = lastname
        member.age = int(age)
        member.gender = gender
        member.weight = float(weight)
        member.adress = adress
        member.email = email
        member.mobile = mobile

        return member
    
    def UpdatePasswordForm(self):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Update Password")
        newPassword = input("Enter new password: \n")
        return newPassword
from Logger import log
from MenuForms import MenuForms
from User import Consultant, SystemAdmin
from Utilities import Utilities
from Database import DatabaseManager


class MenuFunctions:
    
    def __init__(self, logged_in_user):
        self.logged_in_user = logged_in_user
        self.menuForm = MenuForms(self.logged_in_user)
        self.utilities = Utilities()
        

    def UserProfile(self):
        if(self.logged_in_user.typeUser == "SuperAdmin"):
            print(f"Profile:\nUsername: {self.logged_in_user.username} \n")
        else:
            print(f"Profile:")
            print(f"First Name: {self.logged_in_user.firstname}")
            print(f"Last Name: {self.logged_in_user.lastname}")
            print(f"Registration Date: {self.logged_in_user.registrationdate}")

        print("===============================================================\n")    




    def SearchMember(self):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Search Member")
        searchTerm = self.menuForm.SearchTermForm()        
        listMembers = self.logged_in_user.services.GetallMembers()
        foundMembers = self.logged_in_user.services.SearchMembersRecursive(listMembers, searchTerm, [])
        selectedMember = self.menuForm.SelectUserForm(foundMembers)
        return selectedMember

    def AddMember(self):
        member = self.menuForm.MemberForm()
        if(member is not None):
            self.logged_in_user.services.AddMember(member)
        return

    def UpdateMember(self):
        member = self.SearchMember()
        if(member is not None):
            updateMember = self.menuForm.UpdateMemberForm(member)
            self.logged_in_user.services.UpdateMember(updateMember)
        return

    def UpdateCurrentPassword(self):
        newPass = self.menuForm.UpdatePasswordForm()
        self.logged_in_user.services.UpdatePassword(newPass)

    def DeleteMember(self):
        member = self.SearchMember()
        if(member is not None):
            if self.menuForm.DeleteUserForm(member):
                self.logged_in_user.services.DeleteMember(member)
                print(f"Member: {member.firstname} {member.lastname} deleted")
        return

    def SearchUser(self):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Search User")
        searchTerm = self.menuForm.SearchTermForm()
        listUsers = self.logged_in_user.services.GetAllUsers()
        foundUsers = self.logged_in_user.services.SearchUsersRecursive(listUsers, searchTerm, [])
        selectedUser = self.menuForm.SelectUserForm(foundUsers)
        return selectedUser

    def AddConsultant(self):
        consultant = self.menuForm.UserForm(Consultant())
        if(consultant is not None):
            self.logged_in_user.services.AddConsultant(consultant)
        return

    def UpdateConsultant(self):
        consultant = self.SearchUser()
        if(consultant is not None):
            updateConId = self.logged_in_user.services.GetConsultantId(consultant)
            updatecons = self.menuForm.UpdateConsultantForm(consultant)
            self.logged_in_user.services.UpdateConsultant(updatecons, updateConId)
        return

    def ResetConsultant(self):
        consultant = self.SearchUser()
        if(consultant is not None):
            resetcon = self.menuForm.ResetConsultantForm(consultant)
            self.logged_in_user.services.ResetConsultantPassword(resetcon)
        return

    def DeleteConsultant(self):
        consultant = self.SearchUser()
        if(consultant is not None):
            if self.menuForm.DeleteUserForm(consultant):
                self.logged_in_user.services.DeleteConsultant(consultant)
                print(f"{consultant.typeUser}: {consultant.username} deleted")
        return

    def AddAdmin(self):
        systemAdmin = self.menuForm.UserForm(SystemAdmin())
        if(systemAdmin is not None):
            self.logged_in_user.services.AddAdmin(systemAdmin)
        return

    def UpdateAdmin(self):
        systemadmin = self.SearchUser()
        if(systemadmin is not None):
            updateAdminId = self.logged_in_user.services.GetSystemAdminId(systemadmin)
            updateadmin = self.menuForm.UpdateAdminForm(systemadmin)
            print(updateAdminId)
            self.logged_in_user.services.UpdateAdmin(updateadmin, updateAdminId)
        return

    def ResetAdmin(self):
        systemAdmin = self.SearchUser()
        if(systemAdmin is not None):
            resetadmin = self.menuForm.ResetAdminForm(systemAdmin)
            self.logged_in_user.services.ResetAdminPassword(resetadmin)
        return

    def DeleteAdmin(self):
        systemAdmin = self.SearchUser()
        if(systemAdmin is not None):
            if self.menuForm.DeleteUserForm(systemAdmin):
                self.logged_in_user.services.DeleteAdmin(systemAdmin)
                print(f"{systemAdmin.typeUser}: {systemAdmin.username} deleted")
        return

    def CreateBackUp(self):
        return

    def RetrieveBackup(self):
        return

    def SearchLog(self):
        pass
        #logViewer()

    def LogOut(self, isUserLoggedIn):
        isUserLoggedIn =  False
        #ConsoleSafety(LoginMenu)
        return isUserLoggedIn
    
    def CloseApplication(self):
        self.utilities.QuitApplication()
        return


class MenuController:
    menuFunctions = None

    def __init__(self):
        self.dbMan = DatabaseManager()
        self.utilities = Utilities()
        self.logged_in_user = None
        
        self.canShowMenu = True
        self.userLoggedIn = False
    
    consultantMenu = [
        "Search member",
        "Add member",
        "Update member",
        "Update password",
        "Log Out"
    ]
    systemAdminMenu = [
        "Search member",
        "Add member",
        "Update member",
        "Delete member",
        "Search user",
        "Add consultant",
        "Update consultant",
        "Delete consultant",
        "Password reset consultant",
        "Update Password",
        "Create Back Up",
        "Retrieve Back Up",
        "View Logs",
        "Log Out"
    ]
    superAdminMenu = [
        "Search member",
        "Add member",
        "Update member",
        "Delete member",
        "Search user",
        "Add consultant",
        "Password reset consultant",
        "Update consultant",
        "Delete consultant",
        "Add system admin",
        "Update system admin",
        "Delete system admin",
        "Password reset system admin",
        "Create Back Up",
        "Retrieve Back Up",
        "View Logs",
        "Log Out"
    ]

    def CreateMenu(self, arr):
        self.menuFunctions.UserProfile()
        self.utilities.PrintMenuTitle("Menu")
        index = 1
        for item in arr:
            print(str(index) + " " + item)
            index+=1
    
      

    def ViewConsultantMenu(self):
        self.CreateMenu(self.consultantMenu)
        self.ConsultantMenuSelection(self.consultantMenu)
    
    def ConsultantMenuSelection(self, arr):
        index = 1
        for item in arr:
            index+=1
        print("===============================")
        selectedOption = input( "Select option: (Press x to quit)\n")
        if(selectedOption == "x"):
            self.menuFunctions.CloseApplication()
            self.canShowMenu = False
        else:
            try: 
               selectedOption = int(selectedOption)
            except Exception:
                print("Invalid selection! Retry!")
                self.ViewConsultantMenu() 
            else:
                if selectedOption < index:
                    if selectedOption == 1:
                        self.menuFunctions.SearchMember()
                    elif selectedOption == 2:
                        self.menuFunctions.AddMember()
                    elif selectedOption == 3:
                        self.menuFunctions.UpdateMember()
                    elif selectedOption == 4:
                        self.menuFunctions.UpdateCurrentPassword()
                    elif selectedOption == 5:
                        self.userLoggedIn = self.menuFunctions.LogOut(self.userLoggedIn)
                else:
                    print("Invalid selection! Retry!")
                    self.ViewConsultantMenu()         

    
    def ViewSystemAdminMenu(self):
        self.CreateMenu(self.systemAdminMenu)
        self.SystemAdminMenuSelection(self.systemAdminMenu)
    
    def SystemAdminMenuSelection(self, arr):
        index = 1
        for item in arr:
            index+=1
        print("===============================")
        selectedOption = input( "Select option: (Press x to quit)\n")
        if(selectedOption == "x"):
            self.menuFunctions.CloseApplication()
            self.canShowMenu = False
        else:
            try: 
               selectedOption = int(selectedOption)
            except Exception:
                print("Invalid selection! Retry!")
                self.ViewSystemAdminMenu() 
            else:
                if selectedOption < index:
                    if selectedOption == 1:
                        self.menuFunctions.SearchMember()
                    elif selectedOption == 2:
                        self.menuFunctions.AddMember()
                    elif selectedOption == 3:
                        self.menuFunctions.UpdateMember()
                    elif selectedOption == 4:
                        self.menuFunctions.DeleteMember()
                    elif selectedOption == 5:
                        self.menuFunctions.SearchUser()
                    elif selectedOption == 6:
                        self.menuFunctions.AddConsultant()
                    elif selectedOption == 7:
                        self.menuFunctions.UpdateConsultant()
                    elif selectedOption == 8:
                        self.menuFunctions.DeleteConsultant()
                    elif selectedOption == 9:
                        self.menuFunctions.ResetConsultant()
                    elif selectedOption == 10:
                        self.menuFunctions.UpdateCurrentPassword()
                    elif selectedOption == 11:
                        self.menuFunctions.CreateBackUp()
                    elif selectedOption == 12:
                        self.menuFunctions.RetrieveBackup()
                    elif selectedOption == 13:
                        self.menuFunctions.SearchLog()
                    elif selectedOption == 14:
                        self.userLoggedIn = self.menuFunctions.LogOut(self.userLoggedIn)
                else:
                    print("Invalid selection! Retry!")
                    self.ViewSystemAdminMenu()  

    def ViewSuperAdminMenu(self):
        self.CreateMenu(self.superAdminMenu)
        self.SuperAdminMenuSelection(self.superAdminMenu)
    
    def SuperAdminMenuSelection(self, arr):
        index = 1
        for item in arr:
            index+=1
        print("===============================")
        selectedOption = input( "Select option: (Press x to quit)\n")
        
        if(selectedOption == "x"):
            self.menuFunctions.CloseApplication()
            self.canShowMenu = False
        else:
            try: 
               selectedOption = int(selectedOption)
            except Exception:
                print("Invalid selection! Retry!")
                self.ViewSuperAdminMenu()
            else:
                if selectedOption < index:
                    if selectedOption == 1:
                        self.menuFunctions.SearchMember()
                    elif selectedOption == 2:
                        self.menuFunctions.AddMember()
                    elif selectedOption == 3:
                        self.menuFunctions.UpdateMember()
                    elif selectedOption == 4:
                        self.menuFunctions.DeleteMember()
                    elif selectedOption == 5:
                        self.menuFunctions.SearchUser()
                    elif selectedOption == 6:
                        self.menuFunctions.AddConsultant()
                    elif selectedOption == 7:
                        self.menuFunctions.ResetConsultant()
                    elif selectedOption == 8:
                        self.menuFunctions.UpdateConsultant()
                    elif selectedOption == 9:
                        self.menuFunctions.DeleteConsultant()
                    elif selectedOption == 10:
                        self.menuFunctions.AddAdmin()
                    elif selectedOption == 11:
                        self.menuFunctions.UpdateAdmin()
                    elif selectedOption == 12:
                        self.menuFunctions.DeleteAdmin()
                    elif selectedOption == 13:
                        self.menuFunctions.ResetAdmin()
                    elif selectedOption == 14:
                        self.menuFunctions.CreateBackUp()
                    elif selectedOption == 15:
                        self.menuFunctions.RetrieveBackup()
                    elif selectedOption == 16:
                        self.menuFunctions.SearchLog()
                    elif selectedOption == 17:
                        self.userLoggedIn = self.menuFunctions.LogOut(self.userLoggedIn)
                else:
                    print("Invalid selection! Retry!")
                    self.ViewSuperAdminMenu()

    def LoginMenu(self):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Login")
        print("Type 'close' in username to quit")
        username = input("Enter username: ")

        if username.lower() == "close":
            self.utilities.QuitApplication()
            return
        
        password = input("Enter password: ")
        

        if username and password:
            self.user_found, self.logged_in_user = self.dbMan.loginUser(username, password)
            if not self.user_found:
                print("Invalid username or password. Please try again.")
                self.utilities.SleepConsole(1.1)
                self.LoginMenu()
            else:
                
                self.menuFunctions = MenuFunctions(self.logged_in_user)
                if self.logged_in_user.typeUser == "SuperAdmin":
                    print(f"\nLogin successful as Super Admin: {self.logged_in_user.username}")
                    log(self.logged_in_user.username,"Logged in")
                    self.utilities.SleepConsole(1.1)
                    self.ViewMenu()

                    
                    #ConsoleSafety(HomeMenu)
                
                if self.logged_in_user.typeUser == "SystemAdmin":
                    print(f"\nLogin successful as Administrator: {self.logged_in_user.username}")
                    log(self.logged_in_user.username,"Logged in")
                    self.utilities.SleepConsole(1.1)
                    self.ViewMenu()


                    #ConsoleSafety(HomeMenu)

                if self.logged_in_user.typeUser == "Consultant":
                    print(f"\nLogin successful as Consultant: {self.logged_in_user.username}")
                    log(self.logged_in_user.username,"Logged in")
                    self.utilities.SleepConsole(1.1)

                    self.ViewMenu()
                    #ConsoleSafety(HomeMenu)
        else:
            print("Username and password cannot be empty.")
            self.LoginMenu()

    def ViewMenu(self):
        self.userLoggedIn = True
        self.menu = None
        if self.logged_in_user.typeUser == "SuperAdmin":
            self.menu = self.ViewSuperAdminMenu
        if self.logged_in_user.typeUser == "SystemAdmin":
            self.menu = self.ViewSystemAdminMenu
        if self.logged_in_user.typeUser == "Consultant":
            self.menu = self.ViewConsultantMenu
        while(self.canShowMenu):
            self.utilities.ClearConsole()
            self.menu()
            if(not self.userLoggedIn):
                self.logged_in_user = None
                self.LoginMenu()
                break  

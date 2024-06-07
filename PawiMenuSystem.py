import time
from Logger import log
from MenuForms import MenuForms
from User import Consultant, SystemAdmin
from rodeDatabase import DatabaseManager


logged_in_user = None
isUserLoggedIn = False
dbMan = DatabaseManager()
def LoginMenu():
    global logged_in_user, isUserLoggedIn
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username and password:
        user_found, logged_in_user = dbMan.loginUser(username, password)
        
        if not user_found:
            print("Invalid username or password. Please try again.")
        else:
            isUserLoggedIn = True
            if logged_in_user.typeUser == "SuperAdmin":
                print("\nLogin successful as Super Admin")
                log("Super Admin","Logged in")
                time.sleep(2)
                #ConsoleSafety(HomeMenu)
            
            if logged_in_user.typeUser == "SystemAdmin":
                print(f"\nLogin successful as Administrator: {logged_in_user.username}")
                log(logged_in_user.username,"Logged in")
                time.sleep(2)
                #ConsoleSafety(HomeMenu)

            if logged_in_user.typeUser == "Consultant":
                print(f"\nLogin successful as Consultant: {logged_in_user.username}")
                log(logged_in_user.username,"Logged in")
                time.sleep(2)
                #ConsoleSafety(HomeMenu)
    else:
        print("Username and password cannot be empty.")



class MenuFunctions:
    global logged_in_user, dbMan
    def __init__(self):
        self.menuForm = MenuForms()
        
    def SearchMember(self):
        searchTerm = self.menuForm.SearchTermForm()
        listMembers = logged_in_user.services.GetallMembers()
        foundMembers = logged_in_user.services.SearchMembersRecursive(listMembers, searchTerm)
        selectedMember = self.menuForm.SelectUserForm(foundMembers)
        return selectedMember

    def AddMember(self):
        member = self.menuForm.MemberForm()
        logged_in_user.services.AddMember(member)
        return

    def UpdateMember(self):
        member = self.SearchMember()
        updateMember = self.menuForm.UpdateMemberForm(member)
        logged_in_user.services.UpdateMember(updateMember)
        return

    def UpdateCurrentPassword(self):
        newPass = self.menuForm.UpdatePasswordForm()
        logged_in_user.services.UpdatePassword(newPass)

    def DeleteMember(self):
        member = self.SearchMember()
        if self.menuForm.DeleteUserForm(member):
            logged_in_user.services.DeleteMember(member)
            print(f"Member: {member.firstname} {member.lastname} deleted")
        return

    def SearchUser(self):
        searchTerm = self.menuForm.SearchTermForm()
        listUsers = logged_in_user.services.GetAllUsers()
        foundUsers = logged_in_user.services.SearchUsersRecursive(listUsers, searchTerm)
        selectedUser = self.menuForm.SelectUserForm(foundUsers)
        return selectedUser

    def AddConsultant(self):
        consultant = self.menuForm.UserForm(Consultant())
        logged_in_user.services.AddConsultant(consultant)
        return

    def UpdateConsultant(self):
        consultant = self.SearchUser()
        updateConId = logged_in_user.services.GetConsultantId(consultant)
        updatecons = self.menuForm.UpdateConsultantForm(consultant)
        logged_in_user.services.UpdateConsultant(updatecons, updateConId)
        return

    def ResetConsultant(self):
        consultant = self.SearchUser()
        resetcon = self.menuForm.ResetConsultantForm(consultant)
        logged_in_user.services.ResetConsultantPassword(resetcon)
        return

    def DeleteConsultant(self):
        consultant = self.SearchUser()
        if self.menuForm.DeleteUserForm(consultant):
            logged_in_user.services.DeleteConsultant(consultant)
            print(f"{consultant.typeUser}: {consultant.username} deleted")
        return

    def AddAdmin(self):
        systemAdmin = self.menuForm.UserForm(SystemAdmin())
        logged_in_user.services.AddAdmin(systemAdmin)
        return

    def UpdateAdmin(self):
        systemadmin = self.SearchUser()
        updateAdminId = logged_in_user.services.GetSystemAdminId(systemadmin)
        updateadmin = self.menuForm.UpdateAdminForm(systemadmin)
        print(updateAdminId)
        logged_in_user.services.UpdateAdmin(updateadmin, updateAdminId)
        return

    def ResetAdmin(self):
        systemAdmin = self.SearchUser()
        resetadmin = self.menuForm.ResetAdminForm(systemAdmin)
        logged_in_user.services.ResetAdminPassword(resetadmin)
        return

    def DeleteAdmin(self):
        systemAdmin = self.SearchUser()
        if self.menuForm.DeleteUserForm(systemAdmin):
            logged_in_user.services.DeleteAdmin(systemAdmin)
            print(f"{systemAdmin.typeUser}: {systemAdmin.username} deleted")
        return

    def CreateBackUp(self):
        return

    def RetrieveBackup(self):
        return

    def SearchLog(self):
        pass
        #logViewer()

    def LogOut(self):
        global logged_in_user
        logged_in_user = None
        #ConsoleSafety(LoginMenu)
        return


class MenuItem:
    def __init__(self):
        self.menuFunctions = MenuFunctions()
        self.canShowMenu = True
    
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
                        self.menuFunctions.LogOut()
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
                        self.menuFunctions.LogOut()
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
                        self.menuFunctions.LogOut()
                else:
                    print("Invalid selection! Retry!")
                    self.ViewSuperAdminMenu()  

menu = MenuItem()
LoginMenu()
if(isUserLoggedIn):
        
    while(menu.canShowMenu):
        #menu.ViewConsultantMenu()
        #menu.ViewSuperAdminMenu()
        #menu.ViewSystemAdminMenu()
        if logged_in_user.typeUser == "Consultant":
            menu.ViewConsultantMenu()
            
        if logged_in_user.typeUser == "SystemAdmin":
            menu.ViewSystemAdminMenu()

        if logged_in_user.typeUser == "SuperAdmin":
            menu.ViewSuperAdminMenu()
            
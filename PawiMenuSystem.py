from MenuForms import MenuForms
from User import Consultant, SystemAdmin
from Utilities import Utilities

# consultants and system admins should have profiles, in addition to their usernames and 
# passwords. Their profiles contain only first name, last name, 
# and registration date.
class MenuFunctions:
    
    def __init__(self, logged_in_user):
        self.menuForm = MenuForms()
        self.logged_in_user = logged_in_user
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
        foundMembers = self.logged_in_user.services.SearchMembersRecursive(listMembers, searchTerm)
        selectedMember = self.menuForm.SelectUserForm(foundMembers)
        return selectedMember

    def AddMember(self):
        member = self.menuForm.MemberForm()
        self.logged_in_user.services.AddMember(member)
        return

    def UpdateMember(self):
        member = self.SearchMember()
        updateMember = self.menuForm.UpdateMemberForm(member)
        self.logged_in_user.services.UpdateMember(updateMember)
        return

    def UpdateCurrentPassword(self):
        newPass = self.menuForm.UpdatePasswordForm()
        self.logged_in_user.services.UpdatePassword(newPass)

    def DeleteMember(self):
        member = self.SearchMember()
        if self.menuForm.DeleteUserForm(member):
            self.logged_in_user.services.DeleteMember(member)
            print(f"Member: {member.firstname} {member.lastname} deleted")
        return

    def SearchUser(self):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Search User")
        searchTerm = self.menuForm.SearchTermForm()
        listUsers = self.logged_in_user.services.GetAllUsers()
        foundUsers = self.logged_in_user.services.SearchUsersRecursive(listUsers, searchTerm)
        selectedUser = self.menuForm.SelectUserForm(foundUsers)
        return selectedUser

    def AddConsultant(self):
        consultant = self.menuForm.UserForm(Consultant())
        self.logged_in_user.services.AddConsultant(consultant)
        return

    def UpdateConsultant(self):
        consultant = self.SearchUser()
        updateConId = self.logged_in_user.services.GetConsultantId(consultant)
        updatecons = self.menuForm.UpdateConsultantForm(consultant)
        self.logged_in_user.services.UpdateConsultant(updatecons, updateConId)
        return

    def ResetConsultant(self):
        consultant = self.SearchUser()
        resetcon = self.menuForm.ResetConsultantForm(consultant)
        self.logged_in_user.services.ResetConsultantPassword(resetcon)
        return

    def DeleteConsultant(self):
        consultant = self.SearchUser()
        if self.menuForm.DeleteUserForm(consultant):
            self.logged_in_user.services.DeleteConsultant(consultant)
            print(f"{consultant.typeUser}: {consultant.username} deleted")
        return

    def AddAdmin(self):
        systemAdmin = self.menuForm.UserForm(SystemAdmin())
        self.logged_in_user.services.AddAdmin(systemAdmin)
        return

    def UpdateAdmin(self):
        systemadmin = self.SearchUser()
        updateAdminId = self.logged_in_user.services.GetSystemAdminId(systemadmin)
        updateadmin = self.menuForm.UpdateAdminForm(systemadmin)
        print(updateAdminId)
        self.logged_in_user.services.UpdateAdmin(updateadmin, updateAdminId)
        return

    def ResetAdmin(self):
        systemAdmin = self.SearchUser()
        resetadmin = self.menuForm.ResetAdminForm(systemAdmin)
        self.logged_in_user.services.ResetAdminPassword(resetadmin)
        return

    def DeleteAdmin(self):
        systemAdmin = self.SearchUser()
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
    def __init__(self, user):
        self.user = user
        self.menuFunctions = MenuFunctions(self.user)
        self.canShowMenu = True
        self.userLoggedIn = False
        self.utilities = Utilities()
    
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

# menu = MenuItem()
# LoginMenu()
# if(isUserLoggedIn):
        
#     while(menu.canShowMenu):
#         #menu.ViewConsultantMenu()
#         #menu.ViewSuperAdminMenu()
#         #menu.ViewSystemAdminMenu()
#         if self.logged_in_user.typeUser == "Consultant":
#             menu.ViewConsultantMenu()
            
#         if self.logged_in_user.typeUser == "SystemAdmin":
#             menu.ViewSystemAdminMenu()

#         if self.logged_in_user.typeUser == "SuperAdmin":
#             menu.ViewSuperAdminMenu()
            
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
        self.PrintMember(member)
        return

    def UpdateMember(self, member = None):
        if(member is None):
            member = self.SearchMember()
        if(member is not None):
            updateMember = self.menuForm.UpdateMemberForm(member)
            self.logged_in_user.services.UpdateMember(updateMember)
        self.PrintMember(member)
        return

    def UpdateCurrentPassword(self):
        newPass = self.menuForm.UpdatePasswordForm()
        self.logged_in_user.services.UpdatePassword(newPass)

    def DeleteMember(self, member = None):
        if(member is None):
            member = self.SearchMember()
        if(member is not None):
            if self.menuForm.DeleteUserForm(member):
                self.logged_in_user.services.DeleteMember(member)
                print(f"Member: {member.firstname} {member.lastname} deleted")
                self.utilities.SleepConsole(1.5)
        return

    def GetUsers(self):
        listUsers = self.logged_in_user.services.GetAllUsers()
        selectedUser = self.menuForm.SelectUserForm(listUsers)
        return selectedUser
    
    def SearchUser(self, *args):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Search User")
        searchTerm = self.menuForm.SearchTermForm()
        listUsers = self.logged_in_user.services.GetAllUsers()
        foundUsers = self.logged_in_user.services.SearchUsersRecursive(listUsers, searchTerm, [])
        consultantList = []
        systemAdminList = []
        if args[0] == "Consultant":
            consultantList = [user for user in foundUsers if user.typeUser == "Consultant"]
            selectedUser = self.menuForm.SelectUserForm(consultantList)
        elif args[0] == "System Admin":
            systemAdminList = [user for user in foundUsers if user.typeUser == "SystemAdmin"]
            selectedUser = self.menuForm.SelectUserForm(systemAdminList)
        else:
            selectedUser = self.menuForm.SelectUserForm(foundUsers)
        return selectedUser

    def AddConsultant(self):
        consultant = self.menuForm.UserForm(Consultant())
        if(consultant is not None):
            self.logged_in_user.services.AddConsultant(consultant)
        self.PrintUser(consultant)
        return

    def UpdateConsultant(self, consultant = None):
        if(consultant is None):
            consultant = self.SearchUser("Consultant")
        if(consultant is not None):
            updateConId = self.logged_in_user.services.GetConsultantId(consultant)
            updatecons = self.menuForm.UpdateConsultantForm(consultant)
            self.logged_in_user.services.UpdateConsultant(updatecons, updateConId)
        self.PrintUser(updatecons)
        return

    def ResetConsultant(self, consultant = None):
        if(consultant is None):
            consultant = self.SearchUser("Consultant")
        if(consultant is not None):
            resetcon = self.menuForm.ResetConsultantForm(consultant)
            self.logged_in_user.services.ResetConsultantPassword(resetcon)
        self.PrintUser(resetcon)
        return

    def DeleteConsultant(self, consultant = None):
        if(consultant is None):
            consultant = self.SearchUser("Consultant")
        if(consultant is not None):
            if self.menuForm.DeleteUserForm(consultant):
                self.logged_in_user.services.DeleteConsultant(consultant)
                print(f"{consultant.typeUser}: {consultant.username} deleted")
        return

    def AddAdmin(self):
        systemAdmin = self.menuForm.UserForm(SystemAdmin())
        if(systemAdmin is not None):
            self.logged_in_user.services.AddAdmin(systemAdmin)
        self.PrintUser(systemAdmin)
        return

    def UpdateAdmin(self, systemAdmin = None):
        if(systemAdmin is None):
            systemAdmin = self.SearchUser("System Admin")
        if(systemAdmin is not None):
            updateAdminId = self.logged_in_user.services.GetSystemAdminId(systemAdmin)
            updateadmin = self.menuForm.UpdateAdminForm(systemAdmin)
            print(updateAdminId)
            self.logged_in_user.services.UpdateAdmin(updateadmin, updateAdminId)
        self.PrintUser(updateadmin)
        return

    def ResetAdmin(self, systemAdmin = None):
        if(systemAdmin is None):
            systemAdmin = self.SearchUser("System Admin")
        if(systemAdmin is not None):
            resetadmin = self.menuForm.ResetAdminForm(systemAdmin)
            self.logged_in_user.services.ResetAdminPassword(resetadmin)
        self.PrintUser(resetadmin)
        return

    def DeleteAdmin(self, systemAdmin = None):
        if(systemAdmin is None):
            systemAdmin = self.SearchUser("System Admin")
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
        mess = self.utilities.ConsoleMessage("Logging out...")
        print(mess)
        self.utilities.SleepConsole(1.1)
        return isUserLoggedIn
    
    def CloseApplication(self):
        self.utilities.QuitApplication()
        return
    
    def PrintMember(self, member):
        self.utilities.ClearConsole()
        self.menuForm.PrintMemberForm(member)
        self.utilities.SleepConsole(1.1)    
        return
    
    def PrintUser(self, user):
        self.utilities.ClearConsole()
        self.menuForm.PrintUserForm(user)
        self.utilities.SleepConsole(1.1)    
        return
    
    def UpdateOrDelete(self, *args):
        return self.menuForm.UpdateOrDeleteForm(*args)


class MenuController:
    menuFunctions = None

    def __init__(self):
        self.dbMan = DatabaseManager()
        self.utilities = Utilities()
        self.logged_in_user = None
        
        self.canShowMenu = True
        self.userLoggedIn = False
    
    consultantMenu = [
        "Search Member",
        "Add Member",
        "Update Member",
        "Update Password",
        "Log Out"
    ]
    systemAdminMenu = [
        "Search Member",
        "Add Member",
        "Update Member",
        "Delete Member",
        "View Users",
        "Add Consultant",
        "Update Consultant",
        "Delete Consultant",
        "Password Reset Consultant",
        "Update Password",
        "Create Back Up",
        "Retrieve Back Up",
        "View Logs",
        "Log Out"
    ]
    superAdminMenu = [
        "Search Member",
        "Add Member",
        "Update Member",
        "Delete Member",
        "View Users",
        "Add Consultant",
        "Password Reset Consultant",
        "Update Consultant",
        "Delete Consultant",
        "Add System Admin",
        "Update System Admin",
        "Delete System Admin",
        "Password Reset System Admin",
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
            print(self.utilities.ConsoleMessage(str(index)) + " " + item)
            index+=1
    
      

    def ViewConsultantMenu(self):
        self.utilities.ClearConsole()
        self.CreateMenu(self.consultantMenu)
        self.ConsultantMenuSelection(self.consultantMenu)
    
    def ConsultantMenuSelection(self, arr):
        index = 1
        for item in arr:
            index+=1
        print("===============================")
        try:
            mess = self.utilities.ConsoleMessage("Select option: (Enter x to quit)\n")
            selectedOption = input(mess)
        except KeyboardInterrupt:
            print(self.utilities.ErrorMessage("Invalid Key!"))
            self.utilities.SleepConsole(1.1)
            self.ViewSuperAdminMenu()
        if(selectedOption == "x"):
            self.menuFunctions.CloseApplication()
            self.canShowMenu = False
        else:
            try: 
               selectedOption = int(selectedOption)
            except Exception:
                mess = self.utilities.ErrorMessage("Invalid selection! Retry!")
                print(mess)
                self.utilities.SleepConsole(1.1)
                self.ViewConsultantMenu() 
            else:
                if selectedOption < index:
                    if selectedOption == 1:
                        mem = self.menuFunctions.SearchMember()
                        self.menuFunctions.PrintMember(mem)
                        if(mem is not None):
                            choice = self.menuFunctions.UpdateOrDelete(mem)
                            if choice == 1:
                                self.menuFunctions.UpdateMember(mem)
                            elif choice == 2:
                                self.menuFunctions.DeleteMember(mem)
                        return
                    elif selectedOption == 2:
                        self.menuFunctions.AddMember()
                    elif selectedOption == 3:
                        self.menuFunctions.UpdateMember()
                    elif selectedOption == 4:
                        self.menuFunctions.UpdateCurrentPassword()
                    elif selectedOption == 5:
                        self.userLoggedIn = self.menuFunctions.LogOut(self.userLoggedIn)
                else:
                    mess = self.utilities.ErrorMessage("Invalid selection! Retry!")
                    print(mess)
                    self.utilities.SleepConsole(1.1)
                    self.ViewConsultantMenu()         

    
    def ViewSystemAdminMenu(self):
        self.utilities.ClearConsole()
        self.CreateMenu(self.systemAdminMenu)
        self.SystemAdminMenuSelection(self.systemAdminMenu)
    
    def SystemAdminMenuSelection(self, arr):
        index = 1
        for item in arr:
            index+=1
        print("===============================")
        try:
            mess = self.utilities.ConsoleMessage("Select option: (Enter x to quit)\n")
            selectedOption = input(mess)
        except KeyboardInterrupt:
            print(self.utilities.ErrorMessage("Invalid Key!"))
            self.utilities.SleepConsole(1.1)
            self.ViewSuperAdminMenu()
        if(selectedOption == "x"):
            self.menuFunctions.CloseApplication()
            self.canShowMenu = False
        else:
            try: 
               selectedOption = int(selectedOption)
            except Exception:
                mess = self.utilities.ErrorMessage("Invalid selection! Retry!")
                print(mess)
                self.utilities.SleepConsole(1.1)
                self.ViewSystemAdminMenu() 
            else:
                if selectedOption < index:
                    if selectedOption == 1:
                        mem = self.menuFunctions.SearchMember()
                        self.menuFunctions.PrintMember(mem)
                        if(mem is not None):
                            choice = self.menuFunctions.UpdateOrDelete(mem)
                            if choice == 1:
                                self.menuFunctions.UpdateMember(mem)
                            elif choice == 2:
                                self.menuFunctions.DeleteMember(mem)
                        return
                    elif selectedOption == 2:
                        self.menuFunctions.AddMember()
                    elif selectedOption == 3:
                        self.menuFunctions.UpdateMember()
                    elif selectedOption == 4:
                        self.menuFunctions.DeleteMember()
                    elif selectedOption == 5:
                        user = self.menuFunctions.GetUsers()
                        self.menuFunctions.PrintUser(user)
                        if user is not None:
                            if user.typeUser == "Consultant":
                                choice = self.menuFunctions.UpdateOrDelete(user)   
                                if choice == 1:
                                    self.menuFunctions.UpdateConsultant(user)
                                elif choice == 2:
                                    self.menuFunctions.DeleteConsultant(user)
                                elif choice == 3:
                                    self.menuFunctions.ResetConsultant(user)
                        return
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
                    mess = self.utilities.ErrorMessage("Invalid selection! Retry!")
                    print(mess)
                    self.utilities.SleepConsole(1.1)
                    self.ViewSystemAdminMenu()  

    def ViewSuperAdminMenu(self):
        self.utilities.ClearConsole()
        self.CreateMenu(self.superAdminMenu)
        self.SuperAdminMenuSelection(self.superAdminMenu)
    
    def SuperAdminMenuSelection(self, arr):
        
        index = 1
        for item in arr:
            index+=1
        print("===============================")
        try:
            mess = self.utilities.ConsoleMessage("Select option: (Enter x to quit)\n")
            selectedOption = input(mess)
        except KeyboardInterrupt:
            print(self.utilities.ErrorMessage("Invalid Key!"))
            self.utilities.SleepConsole(1.1)
            self.ViewSuperAdminMenu()
        
        if(selectedOption == "x"):
            self.menuFunctions.CloseApplication()
            self.canShowMenu = False
        else:
            try: 
               selectedOption = int(selectedOption)
            except ValueError:
                mess = self.utilities.ErrorMessage("Invalid selection! Retry!")
                print(mess)
                self.utilities.SleepConsole(1.1)
                self.ViewSuperAdminMenu()
            else:
                if selectedOption < index:
                    if selectedOption == 1:
                        mem = self.menuFunctions.SearchMember()
                        self.menuFunctions.PrintMember(mem)
                        if(mem is not None):
                            choice = self.menuFunctions.UpdateOrDelete(mem)
                            if choice == 1:
                                self.menuFunctions.UpdateMember(mem)
                            elif choice == 2:
                                self.menuFunctions.DeleteMember(mem)
                        return
                    elif selectedOption == 2:
                        self.menuFunctions.AddMember()
                    elif selectedOption == 3:
                        self.menuFunctions.UpdateMember()
                    elif selectedOption == 4:
                        self.menuFunctions.DeleteMember()
                    elif selectedOption == 5:
                        user = self.menuFunctions.GetUsers()
                        self.menuFunctions.PrintUser(user)
                        if user is not None:
                            choice = self.menuFunctions.UpdateOrDelete(user)   
                            if user.typeUser == "Consultant":
                                if choice == 1:
                                    self.menuFunctions.UpdateConsultant(user)
                                elif choice == 2:
                                    self.menuFunctions.DeleteConsultant(user)
                                elif choice == 3:
                                    self.menuFunctions.ResetConsultant(user)
                            else:
                                if choice == 1:
                                    self.menuFunctions.UpdateAdmin(user)
                                elif choice == 2:
                                    self.menuFunctions.DeleteAdmin(user)
                                elif choice == 3:
                                    self.menuFunctions.ResetAdmin(user)
                        return
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
                    mess = self.utilities.ErrorMessage("Invalid selection! Retry!")
                    print(mess)
                    self.utilities.SleepConsole(1.1)
                    self.ViewSuperAdminMenu()

    def LoginMenu(self):
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Login")
        print(self.utilities.ReturnMessage("Type 'close' in username to quit"))
        

        try:
            usernameMessage = self.utilities.ConsoleMessage("Enter Username: ")
            username = input(usernameMessage)
            if username.lower() == "close":
                self.utilities.QuitApplication()
                return
            passwordMessage = self.utilities.ConsoleMessage("Enter Password: ")
            password = input(passwordMessage)
        except KeyboardInterrupt:
            print(self.utilities.ErrorMessage("Invalid Key!"))
            self.utilities.SleepConsole(1.1)
            return self.LoginMenu()
        
            

        if username and password:
            self.user_found, self.logged_in_user = self.dbMan.loginUser(username, password)
            if not self.user_found:
                print(self.utilities.ErrorMessage("Invalid username or password. Please try again."))
                self.utilities.SleepConsole(1.1)
                self.LoginMenu()
            else:
                
                self.menuFunctions = MenuFunctions(self.logged_in_user)
                if self.logged_in_user.typeUser == "SuperAdmin":
                    success_message = self.utilities.SuccessMessage(f"\nLogin successful as Super Admin: {self.logged_in_user.username}")
                    print(success_message)
                    log(self.logged_in_user.username,"Logged in")
                    self.utilities.SleepConsole(1.1)
                    self.ViewMenu()

                    
                   
                
                if self.logged_in_user.typeUser == "SystemAdmin":
                    print(f"\nLogin successful as Administrator: {self.logged_in_user.username}")
                    log(self.logged_in_user.username,"Logged in")
                    self.utilities.SleepConsole(1.1)
                    self.ViewMenu()


                   

                if self.logged_in_user.typeUser == "Consultant":
                    print(f"\nLogin successful as Consultant: {self.logged_in_user.username}")
                    log(self.logged_in_user.username,"Logged in")
                    self.utilities.SleepConsole(1.1)

                    self.ViewMenu()
                   
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

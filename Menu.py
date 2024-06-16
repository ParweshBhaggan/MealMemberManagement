from Logger import log, logViewer
from MenuForms import MenuForms
from User import Consultant, SystemAdmin
from Utilities import Utilities
from Database import DatabaseManager


class MenuFunctions:
    '''This class handles the functions of interaction with Menu'''
    
    def __init__(self, logged_in_user):
        self.logged_in_user = logged_in_user
        self.menuForm = MenuForms(self.logged_in_user)
        self.utilities = Utilities()
        

    def UserProfile(self):
        '''Displays the logged in user profile'''
        if(self.logged_in_user.typeUser == "SuperAdmin"):
            print(f"Profile:\nUsername: {self.logged_in_user.username} \n")
        else:
            print(f"Profile:")
            print(f"First Name: {self.logged_in_user.firstname}")
            print(f"Last Name: {self.logged_in_user.lastname}")
            print(f"Registration Date: {self.logged_in_user.registrationdate}")

        print("===============================================================\n")    


    

    def SearchMember(self):
        '''Searches specific Members and opens up a selection form to select the specific Member.'''
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Search Member")
        searchTerm = self.menuForm.SearchTermForm()        
        listMembers = self.logged_in_user.services.GetallMembers()
        foundMembers = self.logged_in_user.services.SearchMembersRecursive(listMembers, searchTerm, [])
        selectedMember = self.menuForm.SelectUserForm(foundMembers)
        return selectedMember

    def AddMember(self):
        '''Opens up a memberform to add a Member'''
        member = self.menuForm.MemberForm()
        if(member is not None):
            self.logged_in_user.services.AddMember(member)
        self.PrintMember(member)
        return

    def UpdateMember(self, member = None):
        '''Opens up a memberform to update a Member'''
        if(member is None):
            member = self.SearchMember()
        if(member is not None):
            updateMember = self.menuForm.UpdateMemberForm(member)
            self.logged_in_user.services.UpdateMember(updateMember)
        self.PrintMember(member)
        return

    def UpdateCurrentPasswordSystemAdmin(self):
        '''Opens up a password form to update current user's password'''
        newPass = self.menuForm.UpdatePasswordForm()
        self.logged_in_user.services.UpdatePasswordOwnSystemAdmin(self.logged_in_user,newPass)

    def UpdateCurrentPasswordConsultant(self):
        '''Opens up a password form to update current user's password'''
        newPass = self.menuForm.UpdatePasswordForm()
        self.logged_in_user.services.UpdatePasswordOwnConsultant(self.logged_in_user,newPass)


    def DeleteMember(self, member = None):
        '''Opens up a memberform to delete a Member'''
        if(member is None):
            member = self.SearchMember()
        if(member is not None):
            if self.menuForm.DeleteUserForm(member):
                self.logged_in_user.services.DeleteMember(member)
                print(f"Member: {member.firstname} {member.lastname} deleted")
                self.utilities.SleepConsole(1.5)
            return
        self.PrintMember(None)
        return

    def GetUsers(self):
        '''Displays all the users.'''
        listUsers = self.logged_in_user.services.GetAllUsers()
        selectedUser = self.menuForm.SelectUserForm(listUsers)
        return selectedUser
    
    def SearchUser(self, *args):
        '''Searches specific users and opens up a selection form to select the specific users.'''
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
        '''Opens up a consultantform to add a Consultant'''
        consultant = self.menuForm.UserForm(Consultant())
        if(consultant is not None):
            self.logged_in_user.services.AddConsultant(consultant)
        self.PrintUser(consultant)
        return

    def UpdateConsultant(self, consultant = None):
        '''Opens up a consultantform to Update a Consultant'''
        if(consultant is None):
            consultant = self.SearchUser("Consultant")
        if(consultant is not None):
            updateConId = consultant.id
            updatecons = self.menuForm.UpdateConsultantForm(consultant)
            self.logged_in_user.services.UpdateConsultant(updatecons, updateConId)
            self.PrintUser(updatecons)
            return
        self.PrintUser(None)
        return

    def ResetConsultant(self, consultant = None):
        '''Opens up a consultantform to reset password of a Consultant'''
        if(consultant is None):
            consultant = self.SearchUser("Consultant")
        if(consultant is not None):
            temp_pass = self.utilities.GeneratePassword()
            consultant.password = temp_pass
            self.logged_in_user.services.ResetConsultantPassword(consultant)
            self.PrintUser(consultant)
            print(f"Password for user {consultant.username} has been resetted!")
            print(f"\nTemporary Password:\n{temp_pass}\n")
            print("Copy the password")
            input("Press any key to continue...\n")
            return
        self.PrintUser(None)
        return

    def DeleteConsultant(self, consultant = None):
        '''Opens up a consultantform to delete a Consultant'''
        if(consultant is None):
            consultant = self.SearchUser("Consultant")
        if(consultant is not None):
            if self.menuForm.DeleteUserForm(consultant):
                self.logged_in_user.services.DeleteConsultant(consultant)
                print(f"{consultant.typeUser}: {consultant.username} deleted")
            return
        self.PrintUser(None)
        return

    def AddAdmin(self):
        '''Opens up a system admin form to add a System Admin'''
        systemAdmin = self.menuForm.UserForm(SystemAdmin())
        if(systemAdmin is not None):
            self.logged_in_user.services.AddAdmin(systemAdmin)
        self.PrintUser(systemAdmin)
        return

    def UpdateAdmin(self, systemAdmin = None):
        '''Opens up a system admin form to update a System Admin'''
        if(systemAdmin is None):
            systemAdmin = self.SearchUser("System Admin")
        if(systemAdmin is not None):
            updateAdminId = self.logged_in_user.services.GetSystemAdminId(systemAdmin)
            updateadmin = self.menuForm.UpdateAdminForm(systemAdmin)
            print(updateAdminId)
            self.logged_in_user.services.UpdateAdmin(updateadmin, updateAdminId)
            self.PrintUser(updateadmin)
            return
        self.PrintUser(None)
        return

    def ResetAdmin(self, systemAdmin = None):
        '''Opens up a system admin form to reset password of a System Admin'''

        if(systemAdmin is None):
            systemAdmin = self.SearchUser("System Admin")
        if(systemAdmin is not None):
            temp_pass = self.utilities.GeneratePassword()
            systemAdmin.password = temp_pass
            self.logged_in_user.services.ResetAdminPassword(systemAdmin)
            self.PrintUser(systemAdmin)
            print(f"Password for user {systemAdmin.username} has been resetted!")
            print(f"\nTemporary Password:\n{temp_pass}\n")
            print("Copy the password")
            input("Press any key to continue...\n")
            
            return
        self.PrintUser(None)
        return

    def DeleteAdmin(self, systemAdmin = None):
        '''Opens up a system admin form to delete a System Admin'''
        if(systemAdmin is None):
            systemAdmin = self.SearchUser("System Admin")
        if(systemAdmin is not None):
            if self.menuForm.DeleteUserForm(systemAdmin):
                self.logged_in_user.services.DeleteAdmin(systemAdmin)
                print(f"{systemAdmin.typeUser}: {systemAdmin.username} deleted")
                return
        self.PrintUser(None)
        return

    def CreateBackUp(self):
        '''Opens up a backupform to create a back up'''
        if self.menuForm.CreateBackupForm():
            self.logged_in_user.services.CreateBackup()
        return

    def RetrieveBackup(self):
        '''Opens up a retrieve backup form to retrieve a back up'''
        backups = self.logged_in_user.services.GetBackups()
        backup = self.menuForm.DisplayAndSelectBackups(backups)
        if self.menuForm.RetrieveBackupForm():
            self.logged_in_user.services.RetrieveBackup(backup)
            print(f"Backup '{backup}' restored successfully.")
            self.utilities.SleepConsole(3)
        return

    def ViewLog(self):
        '''Displays the log in the console'''
        self.utilities.ClearConsole()
        logViewer()

    def LogOut(self, isUserLoggedIn):
        '''Logs the current user out.'''
        isUserLoggedIn =  False
        mess = self.utilities.ConsoleMessage("Logging out...")
        print(mess)
        self.utilities.SleepConsole(1.1)
        return isUserLoggedIn
    
    def CloseApplication(self):
        '''Closes the current application'''
        self.utilities.QuitApplication()
        return
    
    def PrintMember(self, member):
        '''Displays a Member to the console'''
        self.utilities.ClearConsole()
        self.menuForm.PrintMemberForm(member)
        self.utilities.SleepConsole(1.1)    
        return
    
    def PrintUser(self, user):
        '''Displays a User to the console'''
        self.utilities.ClearConsole()
        self.menuForm.PrintUserForm(user)
        self.utilities.SleepConsole(1.1)    
        return
    
    def UpdateOrDelete(self, *args):
        '''Opens up an update or delete form after searching for a specific Member/User'''
        return self.menuForm.UpdateOrDeleteForm(*args)


class MenuController:
    '''This handles how the menu is created,displayed and it's interaction.'''
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
        '''Creates a menu view for specific users'''
        self.menuFunctions.UserProfile()
        self.utilities.PrintMenuTitle("Menu")
        index = 1
        for item in arr:
            print(self.utilities.ConsoleMessage(str(index)) + " " + item)
            index+=1
    
      

    def ViewConsultantMenu(self):
        '''Display a menu view for Consultant'''
        self.utilities.ClearConsole()
        self.CreateMenu(self.consultantMenu)
        self.ConsultantMenuSelection(self.consultantMenu)
    
    def ConsultantMenuSelection(self, arr):
        '''Creates the interactions of a menu view for Consultant'''
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
                        self.menuFunctions.UpdateCurrentPasswordConsultant()
                    elif selectedOption == 5:
                        self.userLoggedIn = self.menuFunctions.LogOut(self.userLoggedIn)
                else:
                    mess = self.utilities.ErrorMessage("Invalid selection! Retry!")
                    print(mess)
                    self.utilities.SleepConsole(1.1)
                    self.ViewConsultantMenu()         

    
    def ViewSystemAdminMenu(self):
        '''Display a menu view for System Admin'''

        self.utilities.ClearConsole()
        self.CreateMenu(self.systemAdminMenu)
        self.SystemAdminMenuSelection(self.systemAdminMenu)
    
    def SystemAdminMenuSelection(self, arr):
        '''Creates the interactions of a menu view for System Admin'''

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
                        self.menuFunctions.UpdateCurrentPasswordSystemAdmin()
                    elif selectedOption == 11:
                        self.menuFunctions.CreateBackUp()
                    elif selectedOption == 12:
                        self.menuFunctions.RetrieveBackup()
                    elif selectedOption == 13:
                        self.menuFunctions.ViewLog()
                    elif selectedOption == 14:
                        self.userLoggedIn = self.menuFunctions.LogOut(self.userLoggedIn)
                else:
                    mess = self.utilities.ErrorMessage("Invalid selection! Retry!")
                    print(mess)
                    self.utilities.SleepConsole(1.1)
                    self.ViewSystemAdminMenu()  

    def ViewSuperAdminMenu(self):
        '''Display a menu view for Super Admin'''
        self.utilities.ClearConsole()
        self.CreateMenu(self.superAdminMenu)
        self.SuperAdminMenuSelection(self.superAdminMenu)
    
    def SuperAdminMenuSelection(self, arr):
        '''Creates the interactions of a menu view for Super Admin'''
        
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
                        self.menuFunctions.ViewLog()
                    elif selectedOption == 17:
                        self.userLoggedIn = self.menuFunctions.LogOut(self.userLoggedIn)
                else:
                    mess = self.utilities.ErrorMessage("Invalid selection! Retry!")
                    print(mess)
                    self.utilities.SleepConsole(1.1)
                    self.ViewSuperAdminMenu()

    def LoginMenu(self, *args):
        '''Displays the login menu '''
        self.utilities.ClearConsole()
        self.utilities.PrintMenuTitle("Login")
        print(self.utilities.ReturnMessage("Type 'close' in username to quit"))
        attempts = 0
        if(len(args) > 0):
            attempts = args[0]
        

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
                log("None","Failed log in", f"Invalid username or password: Username: {username}, Password: {password}")
                attempts += 1
                if(attempts >= 3):
                    log("None","Failed log in many times", f"Invalid username or password: Username: {username}, Password: {password}", "Yes")
                    timer = 30
                    print("You have tried many times to log in, please wait 30 seconds to continue")
                    self.utilities.SleepConsole(1)
                    timer -= 1
                    while timer > 0:
                        self.utilities.ClearConsole()
                        print(f"Remaining time: {timer}")
                        self.utilities.SleepConsole(1)
                        timer-= 1
                self.utilities.SleepConsole(1.1)
                self.LoginMenu(attempts)
            else:
                
                self.menuFunctions = MenuFunctions(self.logged_in_user)
                if self.logged_in_user.typeUser == "SuperAdmin":
                    
                    success_message = self.utilities.SuccessMessage(f"\nLogin successful as Super Admin: {self.logged_in_user.username}")
                    print(success_message)
                    log(self.logged_in_user.username,"Logged in")
                    self.utilities.SleepConsole(1.1)
                    self.ViewMenu()

                    
                   
                
                if self.logged_in_user.typeUser == "SystemAdmin":
                    if self.logged_in_user.temp_pass == 1:
                        print("Your password was resetted please enter a new password.")
                        self.utilities.SleepConsole(2)
                        self.menuFunctions.UpdateCurrentPasswordSystemAdmin()
                    print(f"\nLogin successful as Administrator: {self.logged_in_user.username}")
                    log(self.logged_in_user.username,"Logged in")
                    self.utilities.SleepConsole(1.1)
                    self.ViewMenu()


                   

                if self.logged_in_user.typeUser == "Consultant":
                    if self.logged_in_user.temp_pass == 1:
                        print("Your password was resetted please enter a new password.")
                        self.utilities.SleepConsole(2)
                        self.menuFunctions.UpdateCurrentPasswordConsultant()
                    print(f"\nLogin successful as Consultant: {self.logged_in_user.username}")
                    log(self.logged_in_user.username,"Logged in")
                    self.utilities.SleepConsole(1.1)
                    self.ViewMenu()
                   
        else:
            print("Username and password cannot be empty.")
            self.LoginMenu()

    def ViewMenu(self):
        '''Displays the menu of a specific User'''
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


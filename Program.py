from PawiMenuSystem import MenuController


class Program:
    def __init__(self) -> None:
        self.menuController = MenuController()
        self.menuController.LoginMenu()
    
    # def ViewMenu(self, logged_in_user):
    #     self.menuController = MenuController(self.logged_in_user)
    #     self.menuController.userLoggedIn = True
    #     self.menu = None
    #     if logged_in_user.typeUser == "SuperAdmin":
    #         self.menu = self.menuController.ViewSuperAdminMenu
    #     if logged_in_user.typeUser == "SystemAdmin":
    #         self.menu = self.menuController.ViewSystemAdminMenu
    #     if logged_in_user.typeUser == "Consultant":
    #         self.menu = self.menuController.ViewConsultantMenu
    #     #menu = self.menuController.ViewSuperAdminMenu
    #     while(self.menuController.canShowMenu):
    #         self.utilities.ClearConsole()
    #         self.menu()
    #         if(not self.menuController.userLoggedIn):
    #             logged_in_user = None
    #             self.LoginMenu()
    #             break
    
    # def LoginMenu(self):
    #     self.utilities.ClearConsole()
    #     self.utilities.PrintMenuTitle("Login")
    #     print("Type 'close' in username to quit")
    #     username = input("Enter username: ")

    #     if username.lower() == "close":
    #         self.utilities.QuitApplication()
    #         return
        
    #     password = input("Enter password: ")
        

    #     if username and password:
    #         self.user_found, self.logged_in_user = self.dbMan.loginUser(username, password)
            
    #         if not self.user_found:
    #             print("Invalid username or password. Please try again.")
    #             self.utilities.SleepConsole(1.1)
    #             self.LoginMenu()
    #         else:
                
    #             if self.logged_in_user.typeUser == "SuperAdmin":
    #                 print("\nLogin successful as Super Admin")
    #                 log("Super Admin","Logged in")
    #                 self.utilities.SleepConsole(1.1)

    #                 # self.menuController = MenuController(self.logged_in_user)
    #                 # self.menuController.userLoggedIn = True
    #                 # #menu = self.menuController.ViewSuperAdminMenu
    #                 # while(self.menuController.canShowMenu):
    #                 #     self.utilities.ClearConsole()
    #                 #     self.menuController.ViewSuperAdminMenu()
    #                 #     if(not self.menuController.userLoggedIn):
    #                 #         self.logged_in_user = None
    #                 #         self.LoginMenu()
    #                 #         break
    #                 self.ViewMenu(self.logged_in_user)

                    
    #                 #ConsoleSafety(HomeMenu)
                
    #             if self.logged_in_user.typeUser == "SystemAdmin":
    #                 print(f"\nLogin successful as Administrator: {self.logged_in_user.username}")
    #                 log(self.logged_in_user.username,"Logged in")
    #                 self.utilities.SleepConsole(1.1)
                    
    #                 # self.menuController = MenuController(self.logged_in_user)
    #                 # self.menuController.userLoggedIn = True
    #                 # while(self.menuController.canShowMenu):
    #                 #     self.utilities.ClearConsole()
    #                 #     self.menuController.ViewSystemAdminMenu()
    #                 #     if(not self.menuController.userLoggedIn):
    #                 #         self.logged_in_user = None
    #                 #         self.LoginMenu()
    #                 #         break
    #                 self.ViewMenu(self.logged_in_user)


    #                 #ConsoleSafety(HomeMenu)

    #             if self.logged_in_user.typeUser == "Consultant":
    #                 print(f"\nLogin successful as Consultant: {self.logged_in_user.username}")
    #                 log(self.logged_in_user.username,"Logged in")
    #                 self.utilities.SleepConsole(1.1)

    #                 # self.menuController = MenuController(self.logged_in_user)
    #                 # self.menuController.userLoggedIn = True
    #                 # while(self.menuController.canShowMenu):
    #                 #     self.utilities.ClearConsole()
    #                 #     self.menuController.ViewConsultantMenu()
    #                 #     if(not self.menuController.userLoggedIn):
    #                 #         self.logged_in_user = None
    #                 #         self.LoginMenu()
    #                 #         break

    #                 self.ViewMenu(self.logged_in_user)
    #                 #ConsoleSafety(HomeMenu)
    #     else:
    #         print("Username and password cannot be empty.")
    #         self.LoginMenu()

program = Program()


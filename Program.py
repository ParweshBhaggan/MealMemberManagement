from Logger import log
from PawiMenuSystem import MenuController
from Utilities import Utilities
from rodeDatabase import DatabaseManager


class Program:
    def __init__(self) -> None:
        self.dbMan = DatabaseManager()
        self.utilities = Utilities()
        self.logged_in_user = None
        self.LoginMenu()
    
    def LoginMenu(self):
        username = input("Enter username: ")
        password = input("Enter password: ")

        if username and password:
            self.user_found, self.logged_in_user = self.dbMan.loginUser(username, password)
            
            if not self.user_found:
                print("Invalid username or password. Please try again.")
            else:
                self.menuController = MenuController(self.logged_in_user)
                self.menuController.userLoggedIn = True
                if self.logged_in_user.typeUser == "SuperAdmin":
                    print("\nLogin successful as Super Admin")
                    log("Super Admin","Logged in")
                    self.utilities.SleepConsole(2)

                    while(self.menuController.canShowMenu):
                        self.menuController.ViewSuperAdminMenu()
                        if(not self.menuController.userLoggedIn):
                            self.LoginMenu()

                    
                    #ConsoleSafety(HomeMenu)
                
                if self.logged_in_user.typeUser == "SystemAdmin":
                    print(f"\nLogin successful as Administrator: {self.logged_in_user.username}")
                    log(self.logged_in_user.username,"Logged in")
                    self.utilities.SleepConsole(2)


                    while(self.menuController.canShowMenu):
                        self.menuController.ViewSuperAdminMenu()
                        if(not self.menuController.userLoggedIn):
                            self.LoginMenu()


                    #ConsoleSafety(HomeMenu)

                if self.logged_in_user.typeUser == "Consultant":
                    print(f"\nLogin successful as Consultant: {self.logged_in_user.username}")
                    log(self.logged_in_user.username,"Logged in")
                    self.utilities.SleepConsole(2)


                    while(self.menuController.canShowMenu):
                        self.menuController.ViewSuperAdminMenu()
                        if(not self.menuController.userLoggedIn):
                            self.LoginMenu()

                    #ConsoleSafety(HomeMenu)
        else:
            print("Username and password cannot be empty.")

program = Program()
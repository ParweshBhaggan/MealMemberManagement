class MenuItem:
    def __init__(self) -> None:
        pass
    
    consultantMenu = [
        "Search member",
        "Add member",
        "Update member",
        "Update Password",
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
        index = 0
        for item in arr:
            print(index + " " + item)
            index+=1

    def ViewConsultantMenu(self):
        self.CreateMenu(self.consultantMenu)
    
    def ViewSystemAdminMenu(self):
        self.CreateMenu(self.systemAdminMenu)
    def ViewSuperAdminMenu(self):
        self.CreateMenu(self.superAdminMenu)

menu = MenuItem()
menu.ViewConsultantMenu()
menu.ViewSystemAdminMenu()
menu.ViewSuperAdminMenu()


    
        

import time
import os

from Consultant import Consultant
from Logger import logViewer
from Super_Administrator import SuperAdmin
from System_Administrators import SystemAdmin

administrators = [
    SystemAdmin('Rode','Wilson', 'admin', 'admin'),
    SystemAdmin('Roderick','Wil', 'admin1', 'admin'),
    SystemAdmin('Roder','Wils', 'admin2', 'admin')
]
consultants = [
    Consultant('Test','Consultant', 'consultant', 'password'),
    Consultant('Test1','Consultant', 'consultant1', 'password'),
    Consultant('Test2','Consultant', 'consultant2', 'password')
]

def LoginMenu():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username and password:
        user_found = False
        if SuperAdmin.username == username and SuperAdmin.password == password:
            print("Login successful as Super Admin")
            user_found = True
            time.sleep(5)
            #login
            ConsoleSafety(HomeMenu)
        
        for admin in administrators:
            if admin.username == username and admin.password == password:
                print("\nLogin successful as Administrator")
                user_found = True
                time.sleep(5)
                ConsoleSafety(HomeMenu)
                break
        
        for consultant in consultants:
            if consultant.username == username and consultant.password == password:
                print("\nLogin successful as Consultant")
                user_found = True
                time.sleep(5)
                ConsoleSafety(HomeMenu)
                break

        if not user_found:
            print("Invalid username or password. Please try again.")
    else:
        print("Username and password cannot be empty.")

        
def HomeMenu():
    print("Home menu")
    print("1. Search member")
    print("2. Add member")
    print("3. Update member")
    print("4. Delete member")
    print("5. Search user")
    print("6. Add Consultant")
    print("7. Update Consultant")
    print("8. Reset Consultant")
    print("9. Delete Consultant")
    print("10. Add Admin")
    print("11. Update Admin")
    print("12. Reset Admin")
    print("13. Delete Admin")
    print("14. Create Back up")
    print("15. Retrieve Back up")
    print("16. Search logs")
    print("17. Log out")
    print("--------------------------------------------------------------------\n")
    
    try:
        choice = int(input("Enter option: "))
    except Exception as e:
        print("Invalid option")
        HomeMenu()
        return  # Return to stop further execution
    
    if choice == 1:
        SearchMember()
    elif choice == 2:
        AddMember()
    elif choice == 3:
        UpdateMember()
    elif choice == 4:
        DeleteMember()
    elif choice == 5:
        SearchUser()
    elif choice == 6:
        AddConsultant()
    elif choice == 7:
        UpdateConsultant()
    elif choice == 8:
        ResetConsultant()
    elif choice == 9:
        DeleteConsultant()
    elif choice == 10:
        AddAdmin()
    elif choice == 11:
        UpdateAdmin()
    elif choice == 12:
        ResetAdmin()
    elif choice == 13:
        DeleteAdmin()
    elif choice == 14:
        CreateBackUp()
    elif choice == 15:
        RetrieveBackup()
    elif choice == 16:
        SearchLog()
    elif choice == 17:
        LogOut()
    else:
        HomeMenu()

def SearchMember():
    return
def AddMember():
    return
def UpdateMember():
    return
def DeleteMember():
    return
def SearchUser():
    return
def AddConsultant():
    return
def UpdateConsultant():
    return
def ResetConsultant():
    return
def DeleteConsultant():
    return
def AddAdmin():
    return
def UpdateAdmin():
    return
def ResetAdmin():
    return
def DeleteAdmin():
    return
def CreateBackUp():
    return
def RetrieveBackup():
    return
def SearchLog():
    logViewer()
def LogOut():
    return

def ClearConsole():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def ConsoleSafety(func):
    try:
        ClearConsole()
        func()
    except KeyboardInterrupt:
        ClearConsole()
        print("===Retry!===")
        func()

ConsoleSafety(LoginMenu)

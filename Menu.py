import time
import os
from User import*
from MenuForms import MenuForms
from Logger import logViewer
from rodeDatabase import loginUser

menuForm = MenuForms()

logged_in_user = None

def LoginMenu():
    global logged_in_user
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username and password:
        user_found, logged_in_user, user_type = loginUser(username, password)
        if user_type == "SuperAdmin":
            print("\nLogin successful as Super Admin")
            time.sleep(5)
            ConsoleSafety(HomeMenu)
        
        if user_type == "SystemAdmin":
            print(f"\nLogin successful as Administrator: {logged_in_user[3]}")
            time.sleep(5)
            ConsoleSafety(HomeMenu)

        if user_type == "Consultant":
            print(f"\nLogin successful as Consultant: {logged_in_user[3]}")
            time.sleep(5)
            ConsoleSafety(HomeMenu)
        # print(user_type)
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
    consultant = Consultant()
    menuForm.UserForm(consultant)
    return
def UpdateConsultant():
    return
def ResetConsultant():
    return
def DeleteConsultant():
    return
def AddAdmin():
    systemAdmin = SystemAdmin()
    menuForm.UserForm(systemAdmin)
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
    global logged_in_user
    logged_in_user = None
    ConsoleSafety(LoginMenu)
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

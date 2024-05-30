import os

def LoginMenu():
    username = input("Enter username: ")
    password = input("Enter password: ")

    if(username != "" and password != ""):
        #login
        ConsoleSafety(HomeMenu)
        

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


    match(choice):
        case 1: SearchMember()
        case 2: AddMember()
        case 3: UpdateMember()
        case 4: DeleteMember()
        case 5: SearchUser()
        case 6: AddConsultant()
        case 7: UpdateConsultant()
        case 8: ResetConsultant()
        case 9: DeleteConsultant()
        case 10: AddAdmin()
        case 11: UpdateAdmin()
        case 12: ResetAdmin()
        case 13: DeleteAdmin()
        case 14: CreateBackUp()
        case 15: RetrieveBackup
        case 16: SearchLog()
        case 17: LogOut()
    
    if(choice <= 0 or choice > 17):
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
    return
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

import time
import os
from MenuForms import MenuForms
from Logger import log, logViewer
from User import Consultant, SystemAdmin, SuperAdmin
from rodeDatabase import DatabaseManager

menuForm = MenuForms()
logged_in_user = None
dbMan = DatabaseManager()
def LoginMenu():
    global logged_in_user, menuForm
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username and password:
        user_found, logged_in_user = dbMan.loginUser(username, password)
        
        if not user_found:
            print("Invalid username or password. Please try again.")
        else:
            if logged_in_user.typeUser == "SuperAdmin":
                print("\nLogin successful as Super Admin")
                log("Super Admin","Logged in")
                time.sleep(2)
                ConsoleSafety(HomeMenu)
            
            if logged_in_user.typeUser == "SystemAdmin":
                print(f"\nLogin successful as Administrator: {logged_in_user.username}")
                log(logged_in_user.username,"Logged in")
                time.sleep(2)
                ConsoleSafety(HomeMenu)

            if logged_in_user.typeUser == "Consultant":
                print(f"\nLogin successful as Consultant: {logged_in_user.username}")
                log(logged_in_user.username,"Logged in")
                time.sleep(2)
                ConsoleSafety(HomeMenu)
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
    searchTerm = menuForm.SearchTermForm()
    listMembers = logged_in_user.services.GetallMembers()
    foundMembers = logged_in_user.services.SearchMembersRecursive(listMembers, searchTerm)
    selectedMember = menuForm.SelectUserForm(foundMembers)
    return selectedMember
def AddMember():
    member = menuForm.MemberForm()
    logged_in_user.services.AddMember(member)
    return
def UpdateMember():
    member = SearchMember()
    updateMember = menuForm.UpdateMemberForm(member)
    logged_in_user.services.UpdateMember(updateMember)
    return
def DeleteMember():
    member = SearchMember()
    if menuForm.DeleteUserForm(member):
        logged_in_user.services.DeleteMember(member)
        print(f"Member: {member.firstname} {member.lastname} deleted")
    return
def SearchUser():
    searchTerm = menuForm.SearchTermForm()
    listUsers = logged_in_user.services.GetAllUsers()
    foundUsers = logged_in_user.services.SearchUsersRecursive(listUsers, searchTerm)
    selectedUser = menuForm.SelectUserForm(foundUsers)
    return selectedUser
def AddConsultant():
    consultant = menuForm.UserForm(Consultant())
    logged_in_user.services.AddConsultant(consultant)
    return
def UpdateConsultant():
    consultant = SearchUser()
    updateConId = logged_in_user.services.GetConsultantId(consultant)
    updatecons = menuForm.UpdateConsultantForm(consultant)
    logged_in_user.services.UpdateConsultant(updatecons, updateConId)
    return
def ResetConsultant():
    # deze search nog beide users maar kan alleen consultant verwijderen
    consultant = SearchUser()
    resetcon = menuForm.ResetConsultantForm(consultant)
    logged_in_user.services.ResetConsultantPassword(resetcon)
    return
def DeleteConsultant():
    # deze search nog beide users maar kan alleen consultant verwijderen
    consultant = SearchUser()
    if menuForm.DeleteUserForm(consultant):
        logged_in_user.services.DeleteConsultant(consultant)
        print(f"{consultant.typeUser}: {consultant.username} deleted")
    return
def AddAdmin():
    systemAdmin = menuForm.UserForm(SystemAdmin())
    logged_in_user.services.AddAdmin(systemAdmin)
    return
def UpdateAdmin():
    systemadmin = SearchUser()
    updateAdminId = logged_in_user.services.GetSystemAdminId(systemadmin)
    updateadmin = menuForm.UpdateAdminForm(systemadmin)
    print(updateAdminId)
    logged_in_user.services.UpdateAdmin(updateadmin, updateAdminId)
    return
def ResetAdmin():
    systemAdmin = SearchUser()
    resetadmin = menuForm.ResetAdminForm(systemAdmin)
    logged_in_user.services.ResetAdminPassword(resetadmin)
    return
def DeleteAdmin():
    # deze search nog beide users maar kan alleen system admin verwijderen
    systemAdmin = SearchUser()
    if menuForm.DeleteUserForm(systemAdmin):
        logged_in_user.services.DeleteAdmin(systemAdmin)
        print(f"{systemAdmin.typeUser}: {systemAdmin.username} deleted")
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


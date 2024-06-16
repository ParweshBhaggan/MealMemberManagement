from Backup import BackupSystem
from Logger import log
from Database import DatabaseManager

class UserServices:
    '''This class handles the services as an abstraction for database services'''
    def __init__(self, user):
        self.user = user
        self.databaseManager = DatabaseManager()
        self.backup = BackupSystem()

    def UpdatePasswordOwnSystemAdmin(self, admin, newpassword):
        '''Service for updating password'''
        admin.password = newpassword
        self.databaseManager.UpdatePasswordOwnSystemAdmin(admin)
        log(self.user.username, f'Updated password.', f'{self.user.typeUser}: {self.user.username} changed his password')

    def UpdatePasswordOwnConsultant(self, consultant, newpassword):
        '''Service for updating password'''
        consultant.password = newpassword
        self.databaseManager.UpdatePasswordOwnConsultant(consultant)
        log(self.user.username, f'Updated password.', f'{self.user.typeUser}: {self.user.username} changed his password')


    def GetAllUsers(self):
        '''Service for retrieving all Users'''
        return self.databaseManager.getallUsers()
    
    def AddAdmin(self, admin):
        '''Service for adding a System Admin'''
        self.databaseManager.createSystemAdmin(admin)
        log(self.user.username, f'New user: {admin.typeUser} is created.', f'username: "{admin.username}"')
    
    def DeleteAdmin(self, admin):
        '''Service for deleting a System Admin'''
        self.databaseManager.deleteSystemAdmin(admin)
        log(self.user.username, f'User: {admin.typeUser} is deleted.', f'User: "{admin.username}" is deleted')

    def UpdateAdmin(self, admin, id):
        '''Service for updating a System Admin'''
        self.databaseManager.updateSystemAdmin(admin, id)
        log(self.user.username, f'User: {admin.typeUser} is updated.', f'User: "{admin.username}"')
    
    def ResetAdminPassword(self,admin):
        '''Service for resetting password of a System Admin'''
        self.databaseManager.resetSystemAdminPassword(admin)
        log(self.user.username, f'User: {admin.typeUser} password updated.', f'{admin.typeUser}: "{admin.username}" password is updated')

    def AddConsultant(self, consultant):
        '''Service for adding a Consultant'''
        self.databaseManager.createConsultant(consultant)
        log(self.user.username, f'New user: {consultant.typeUser} is created.', f'username: "{consultant.username}"')

    def DeleteConsultant(self, consultant):
        '''Service for deleting a Consultant'''
        self.databaseManager.deleteConsultant(consultant)
        log(self.user.username, f'User: {consultant.typeUser} is deleted.', f'User: "{consultant.username}" is deleted')
    
    def UpdateConsultant(self, consultant, id):
        '''Service for updating a Consultant'''
        self.databaseManager.updateConsultant(consultant, id)
        log(self.user.username, f'User: {consultant.typeUser} is updated.', f'User: "{consultant.username}"')


    def ResetConsultantPassword(self, consultant):
        '''Service for resetting a password of a Consultant'''
        self.databaseManager.resetConsultantPassword(consultant)
        log(self.user.username, f'User: {consultant.typeUser} password updated.', f'{consultant.typeUser}: "{consultant.username}" password is updated')

    def GetallMembers(self):
        '''Service for retrieving all Members'''
        return self.databaseManager.getallMembers()

    def AddMember(self, member):
        '''Service for adding a Member'''
        self.databaseManager.createMember(member)
        log(self.user.username, f'New user: Member is created.', f'firstname: "{member.firstname}", lastname: "{member.lastname}"')

    def DeleteMember(self, member):
        '''Service for deleting a Member'''
        self.databaseManager.deleteMember(member)
        log(self.user.username, f'User: Member is deleted.', f'User: firstname: "{member.firstname}", lastname: "{member.lastname}" is deleted')

    def UpdateMember(self, member):
        '''Service for updating a Member'''
        self.databaseManager.updateMember(member)
        log(self.user.username, f'User: Member is updated.', f'User: firstname: "{member.firstname}", lastname: "{member.lastname}" is updated')
    
    def SearchMembersRecursive(self, members, searchVal, foundMember=[], itemIndex=0):
        '''Service for searching a Member'''
        if itemIndex >= len(members):
            return foundMember
        getMemberAttr = list(members[itemIndex].__dict__.values())
        for attr in range(0, len(getMemberAttr) - 1):
           
            if str(getMemberAttr[attr]).lower().__contains__(searchVal.lower()):
                foundMember.append(members[itemIndex])
                break
        return self.SearchMembersRecursive(members, searchVal, foundMember, itemIndex + 1)
    
    def SearchUsersRecursive(self, users, searchVal="",foundUser=[], itemIndex=0):
        '''Service for searching a User'''
        if searchVal == "":
            searchVal = input("Search: ")
            
        if itemIndex >= len(users):
            return foundUser
        getUserAttr = list(users[itemIndex].__dict__.values())
        for attr in range(0, len(getUserAttr) - 4):
          
            if str(getUserAttr[attr]).lower().__contains__(searchVal.lower()):
                foundUser.append(users[itemIndex])
                break
        return self.SearchUsersRecursive(users, searchVal, foundUser, itemIndex + 1)

    def GetSystemAdminId(self, user):
        '''Service for retrieving specific ID of a System Admin'''
        id = self.databaseManager.FetchSystemAdminID(user)
        return id

    def GetConsultantId(self, user):
        '''Service for retrieving specific ID of a Consultant'''
        id = self.databaseManager.FetchConsultantID(user)
        return id

    def CheckMemberMobile(self, mobileNumber):
        '''Service for checking existing Mobile number of a Member'''
        mobile = self.databaseManager.FetchMemberMobile(mobileNumber)
        if mobile is not None:
            print(f"Number exists!!!")
            return True
        return False

    def CheckMemberEmail(self, emailAddress):
        '''Service for checking existing Email adress of a Member'''
        email = self.databaseManager.FetchMemberEmail(emailAddress)
        if email is not None:
            print(f"Email exists!!!")
            return True
        return False
    
    def CheckUsername(self, name, username):
        '''Service for checking existing Username of a System Admin'''
        if(name == "SystemAdmin"):
            user_username = self.databaseManager.FetchAdminUsername(username)
        elif(name == "Consultant"):
            user_username = self.databaseManager.FetchConsUsername(username)
        if user_username is not None:
            print(f"Username exists!!!")
            return True
        return False

    def GetUsernameUsers(self, ListUser):
        '''Service for retrieving Users from a list'''
        if len(ListUser) > 0:
            for user in ListUser:
                print(user.firstname, user.lastname, user.username, user.password, user.registrationdate)

   
    def CreateBackup(self):
        '''Service for creating a back up'''
        self.backup.create_backup()
        log(self.user.username, "Backup created.", "Backup created.")

    def RetrieveBackup(self, backup):
        '''Service for restoring a back up'''
        self.backup.restore(backup)
        log(self.user.username, f"Backup restored.", f"'{backup}' retrieved.")

    def GetBackups(self):
        '''Service for retrieving multiple back ups'''
        return self.backup.GetBackupFolders()
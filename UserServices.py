from Backup import BackupSystem
from Logger import log
from Database import DatabaseManager

class UserServices:
    def __init__(self, user):
        self.user = user
        self.databaseManager = DatabaseManager()
        self.backup = BackupSystem()

    def UpdatePassword(self, newpassword):
        self.databaseManager.resetPassword(newpassword, self.user.username)
        log(self.user.username, f'Updated password.', f'{self.user.typeUser}: {self.user.username} changed his password')

    def GetAllUsers(self):
        return self.databaseManager.getallUsers()
    
    def AddAdmin(self, admin):
        self.databaseManager.createSystemAdmin(admin)
        log(self.user.username, f'New user: {admin.typeUser} is created.', f'username: "{admin.username}"')
    
    def DeleteAdmin(self, admin):
        self.databaseManager.deleteSystemAdmin(admin)
        log(self.user.username, f'User: {admin.typeUser} is deleted.', f'User: "{admin.username}" is deleted')

    def UpdateAdmin(self, admin, id):
        self.databaseManager.updateSystemAdmin(admin, id)
        log(self.user.username, f'User: {admin.typeUser} is updated.', f'User: "{admin.username}"')
    
    def ResetAdminPassword(self,admin):
        self.databaseManager.resetSystemAdminPassword(admin)
        log(self.user.username, f'User: {admin.typeUser} password updated.', f'{admin.typeUser}: "{admin.username}" password is updated')

    def AddConsultant(self, consultant):
        self.databaseManager.createConsultant(consultant)
        log(self.user.username, f'New user: {consultant.typeUser} is created.', f'username: "{consultant.username}"')

    def DeleteConsultant(self, consultant):
        self.databaseManager.deleteConsultant(consultant)
        log(self.user.username, f'User: {consultant.typeUser} is deleted.', f'User: "{consultant.username}" is deleted')
    
    def UpdateConsultant(self, consultant, id):
        self.databaseManager.updateConsultant(consultant, id)
        log(self.user.username, f'User: {consultant.typeUser} is updated.', f'User: "{consultant.username}"')


    def ResetConsultantPassword(self, consultant):
        self.databaseManager.resetConsultantPassword(consultant)
        log(self.user.username, f'User: {consultant.typeUser} password updated.', f'{consultant.typeUser}: "{consultant.username}" password is updated')

    def GetallMembers(self):
        return self.databaseManager.getallMembers()

    def AddMember(self, member):
        self.databaseManager.createMember(member)
        log(self.user.username, f'New user: Member is created.', f'firstname: "{member.firstname}", lastname: "{member.lastname}')

    def DeleteMember(self, member):
        self.databaseManager.deleteMember(member)
        log(self.user.username, f'User: Member is deleted.', f'User: firstname: "{member.firstname}", lastname: "{member.lastname} is deleted')

    def UpdateMember(self, member):
        self.databaseManager.updateMember(member)
        log(self.user.username, f'User: Member is updated.', f'User: firstname: "{member.firstname}", lastname: "{member.lastname} is updated')
    
    def SearchMembersRecursive(self, members, searchVal, foundMember=[], itemIndex=0):
        if itemIndex >= len(members):
            return foundMember
        getMemberAttr = list(members[itemIndex].__dict__.values())
        for attr in range(0, len(getMemberAttr) - 1):
            # attr is a value of an item attribute for example: item.firstname = attr[0]
            if str(getMemberAttr[attr]).lower().__contains__(searchVal.lower()):
                foundMember.append(members[itemIndex])
                break
        return self.SearchMembersRecursive(members, searchVal, foundMember, itemIndex + 1)
    
    def SearchUsersRecursive(self, users, searchVal="",foundUser=[], itemIndex=0):
        if searchVal == "":
            searchVal = input("Search: ")
            # return self.SearchRecursive(arr, searchVal, foundUser, itemIndex)
        if itemIndex >= len(users):
            return foundUser
        getUserAttr = list(users[itemIndex].__dict__.values())
        for attr in range(0, len(getUserAttr) - 4):
            # attr is a value of an item attribute for example: item.firstname = attr[0]
            if str(getUserAttr[attr]).lower().__contains__(searchVal.lower()):
                foundUser.append(users[itemIndex])
                break
        return self.SearchUsersRecursive(users, searchVal, foundUser, itemIndex + 1)

    def GetSystemAdminId(self, user):
       id = self.databaseManager.FetchSystemAdminID(user)
       return id

    def GetConsultantId(self, user):
       id = self.databaseManager.FetchConsultantID(user)
       return id

    def CheckMemberMobile(self, mobileNumber):
        mobile = self.databaseManager.FetchMemberMobile(mobileNumber)
        if mobile is not None:
            print(f"Number exists!!!")
            return True
        return False

    def CheckMemberEmail(self, emailAddress):
        email = self.databaseManager.FetchMemberEmail(emailAddress)
        if email is not None:
            print(f"Email exists!!!")
            return True
        return False
    
    def CheckUsername(self, name, username):
        if(name == "SystemAdmin"):
            user_username = self.databaseManager.FetchAdminUsername(username)
        elif(name == "Consultant"):
            user_username = self.databaseManager.FetchConsUsername(username)
        if user_username is not None:
            print(f"Username exists!!!")
            return True
        return False

    def GetUsernameUsers(self, ListUser):
        if len(ListUser) > 0:
            for user in ListUser:
                print(user.firstname, user.lastname, user.username, user.password, user.registrationdate)

    def CheckUsers(self):
        # log('Cheking users...')
        for admin in self.administrators:
            pass
            # log(f'{admin.firstname, admin.lastname, admin.username, admin.password, type(admin)}')
        for consultant in self.consultants: 
            pass
            # log(f'{consultant.firstname, consultant.lastname, consultant.username, consultant.password, type(consultant)}')
        for member in self.members:
            pass
            # log(f'{member.ID, member.firstname, member.lastname, member.username, member.password, member.registrationdate, member.age, member.gender, member.weight, member.adress, member.mobile}')

    def CreateBackup(self):
        self.backup.create_backup()
        log(self.user.username, "Backup created.", "Backup created.")

    def RetrieveBackup(self, backup):
        self.backup.restore(backup)
        log(self.user.username, f"Backup restored.", f"'{backup}' retrieved.")

    def GetBackups(self):
        backup = BackupSystem()
        return backup.backups
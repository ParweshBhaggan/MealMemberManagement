from Logger import log
from rodeDatabase import DatabaseManager

class UserServices:
<<<<<<< HEAD
    consultants = list()
    members = list()
    administrators = list()
    def __init__(self):
        pass

    def updatePassword(self,user, newpassword):
        #print('\nUpdating password')
        oldpassword = user.password
        user.password = newpassword
        #print(self.password)
        log(f'Updated password for User: {user.username}, old password: {oldpassword} to new password: {user.password}')
    
    def addAdmin(self, admin):
        #print('\nAdd Administrator')
        self.administrators.append(admin)
        #print(admin.firstname, admin.lastname)
        log(f'Added administrator {admin.firstname} {admin.lastname} with username: {admin.username}')
    
    def deleteAdmin(self, admin):
        #print('\nDeleting Administrator', admin.firstname)
        self.administrators.remove(admin)
        log(f'Deleted administrator {admin.firstname} {admin.lastname} with username: {admin.username}')

    def updateAdmin(self, admin):
        for adm in self.administrators:
            if adm.username == admin.username:
                #print(f'\nUpdating Administrator {adm.firstname} to {admin.firstname}')
                adm.firstname = admin.firstname
                adm.lastname = admin.lastname
                log(f'Updated administrator {adm.firstname} {adm.lastname} with username: {adm.username}')
    
    def resetAdminPassword(self, newpassword, admin):
        #print(f'\nResetting administrator {admin.firstname} password')
        for adm in self.administrators:
            if adm.username == admin.username:
                log(f'Reset password for administrator {adm.firstname} {adm.lastname} with username: {adm.username}, old password: {adm.password} to new password: {newpassword}')
                adm.password = newpassword
=======
    def __init__(self, user):
        self.user = user
        self.databaseManager = DatabaseManager()

    def UpdatePassword(self, newpassword):
        self.databaseManager.resetPassword(newpassword, self.user.username)
        log(self.user.username, f'Updated password.', f'{self.user.typeUser}: {self.user.username} changed his password')
>>>>>>> de25cdf4061096adabbb51af08895b960367b926

    def GetAllUsers(self):
        return self.databaseManager.getallUsers()
    
    def AddAdmin(self, admin):
        self.databaseManager.createSystemAdmin(admin)
        log(self.user.username, f'New user: {admin.typeUser} is created.', f'username: "{admin.username}"')
    
    def DeleteAdmin(self, admin):
        self.databaseManager.deleteSystemAdmin(admin)
        log(self.user.username, f'User: {admin.typeUser} is deleted.', f'User: "{admin.username}" is deleted')

<<<<<<< HEAD
    def checkUsers(self):
        #print('\nChecking users')
        #print('Administrators')
        log('Cheking users...')
        for admin in self.administrators:
            #print(admin.firstname, admin.lastname, admin.username, admin.password, type(admin))
            log(f'{admin.firstname, admin.lastname, admin.username, admin.password, type(admin)}')
        for consultant in self.consultants:
            #print(consultant.firstname, consultant.lastname, consultant.username, consultant.password, type(consultant))
            log(f'{consultant.firstname, consultant.lastname, consultant.username, consultant.password, type(consultant)}')
        #print('\nMembers')
=======
    def UpdateAdmin(self, admin, id):
        # Moet nog verandert worden
        self.databaseManager.updateSystemAdmin(admin, id)
        #log(f'Updated administrator {adm.firstname} {adm.lastname} with username: {adm.username}')
    
    def ResetAdminPassword(self,admin):
        self.databaseManager.resetSystemAdminPassword(admin)
        log(self.user.username, f'User: {admin.typeUser} password updated.', f'{admin.typeUser}: "{admin.username}" password is updated')

    def AddConsultant(self, consultant):
        self.databaseManager.createConsultant(consultant)
        log(self.user.username, f'New user: {consultant.typUser} is created.', f'username: "{consultant.username}"')

    def DeleteConsultant(self, consultant):
        self.databaseManager.deleteConsultant(consultant)
        log(self.user.username, f'User: {consultant.typeUser} is deleted.', f'User: "{consultant.username}" is deleted')
    
    # Moet nog verandert worden
    def UpdateConsultant(self, consultant, id):
        self.databaseManager.updateConsultant(consultant, id)
        # log(f'Updated consultant {con.firstname} {con.lastname} with username: {con.username}')

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

    # Moet nog verandert worden
    def UpdateMember(self, member):
        self.databaseManager.updateMember(member)
        # log(f'Updated member {mem.firstname} {mem.lastname} with username: {mem.username} ID: {mem.ID}')
    
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
>>>>>>> de25cdf4061096adabbb51af08895b960367b926
        for member in self.members:
            pass
            # log(f'{member.ID, member.firstname, member.lastname, member.username, member.password, member.registrationdate, member.age, member.gender, member.weight, member.adress, member.mobile}')
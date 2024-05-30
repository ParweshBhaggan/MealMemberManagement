from datetime import date
from Logger import log


class UserServices:
    consultants = list()
    members = list()
    administrators = list()
    def __init__(self) -> None:
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

    def addConsultant(self, consultant):
        #print('\nAdd Consultant')
        self.consultants.append(consultant)
        #print(consultant.firstname, consultant.lastname)
        log(f'Added consultant {consultant.firstname} {consultant.lastname} with username: {consultant.username}')

    def deleteConsultant(self, consultant):
        #print('\nDeleting Consultant', consultant.firstname)
        self.consultants.remove(consultant)
        log(f'Deleted consultant {consultant.firstname} {consultant.lastname} with username: {consultant.username}')
        #self.checkUsers()
    
    def updateConsultant(self, consultant):
        for con in self.consultants:
            if con.username == consultant.username:
                #print(f'\nUpdating Consultant {con.firstname} to {consultant.firstname}')
                con.firstname = consultant.firstname
                con.lastname = consultant.lastname
                log(f'Updated consultant {con.firstname} {con.lastname} with username: {con.username}')
        #self.checkUsers()

    def resetConsultantPassword(self, newpassword, consultant):
        #print(f'\nResetting consultant {consultant.firstname} password')
        for con in self.consultants:
            if con.username == consultant.username:
                log(f'Reset password for consultant {con.firstname} {con.lastname} with username: {con.username}, old password: {con.password} to new password: {newpassword}')
                con.password = newpassword
        #self.checkUsers()     

    def addMember(self, member):
        #print('\nAdd Member')
        self.members.append(member)
        #print(member.firstname, member.lastname)
        log(f'Added member {member.firstname} {member.lastname} with username: {member.username} ID: {member.ID}')

    def deleteMember(self, member):
        #print('\nDeleting Member', member.firstname)
        self.members.remove(member)
        log(f'Deleted member {member.firstname} {member.lastname} with username: {member.username} ID: {member.ID}')
        #self.checkUsers()

    def updateMember(self, member):
        for mem in self.members:
            if mem.username == member.username:
                #print(f'\nUpdating Member {mem.firstname} to {member.firstname}')
                mem.firstname = member.firstname
                mem.lastname = member.lastname
                mem.email = member.email
                mem.mobile = member.mobile
                log(f'Updated member {mem.firstname} {mem.lastname} with username: {mem.username} ID: {mem.ID}')
        #self.checkUsers()
    
    def resetMemberPassword(self, newpassword, member):
        #print(f'\nResetting member {member.firstname} password')
        for mem in self.members:
            if mem.username == member.username:
                log(f'Reset password for member {mem.firstname} {mem.lastname} with username: {mem.username} ID: {mem.ID}, old password: {mem.password} to new password: {newpassword}')
                mem.password = newpassword
        #self.checkUsers()
    
    def searchMember(self, memberusername):
        #print(f'\nSearching member with username: {memberusername}')
        for mem in self.members:
            if mem.username == memberusername:
                #print(mem.ID, mem.firstname, mem.lastname, mem.username, mem.password, mem.registrationdate, mem.age, mem.gender, mem.weight, mem.adress, mem.mobile)
                log(f'Searched for member {mem.ID, mem.firstname, mem.lastname, mem.username, mem.password, mem.registrationdate, mem.age, mem.gender, mem.weight, mem.adress, mem.mobile}')

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
        for member in self.members:
            #print(member.firstname, member.lastname, member.username, member.password, type(member))
            log(f'{member.ID, member.firstname, member.lastname, member.username, member.password, member.registrationdate, member.age, member.gender, member.weight, member.adress, member.mobile}')
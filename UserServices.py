from datetime import date
from Logger import log


class UserServices:
    consultants = list()
    members = list()
    def __init__(self) -> None:
        pass

    def updatePassword(self,user, newpassword):
        #print('\nUpdating password')
        oldpassword = user.password
        user.password = newpassword
        #print(self.password)
        log(f'Updated password for SystemAdmin: {user.username}, old password: {oldpassword} to new password: {user.password}')

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
        #print('Consultants')
        log('Cheking users...')
        for consultant in self.consultants:
            #print(consultant.firstname, consultant.lastname, consultant.username, consultant.password, type(consultant))
            log(f'{consultant.firstname, consultant.lastname, consultant.username, consultant.password, type(consultant)}')
        #print('\nMembers')
        for member in self.members:
            #print(member.firstname, member.lastname, member.username, member.password, type(member))
            log(f'{member.ID, member.firstname, member.lastname, member.username, member.password, member.registrationdate, member.age, member.gender, member.weight, member.adress, member.mobile}')
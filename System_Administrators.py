#consultants and system admins should have profiles, in addition to their usernames and passwords.
#Their profiles contain only first name, last name, and registration date.
from datetime import date
from Consultant import Consultant
from Logger import log,logViewer
from Members import Member

"""
● To make a backup of the system and restore a backup (members information and users’ data).

"""

class SystemAdmin:
    consultants = list()
    members = list()
    def __init__(self, firstname, lastname, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.registrationdate = date.today()
        self.username = username
        self.password = password
        log(f'Created SystemAdmin: {self.firstname} {self.lastname} with username: {self.username}')
    
    def updatePassword(self, newpassword):
        #print('\nUpdating password')
        oldpassword = self.password
        self.password = newpassword
        #print(self.password)
        log(f'Updated password for SystemAdmin: {self.username}, old password: {oldpassword} to new password: {self.password}')

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

systemadmin = SystemAdmin('Roderick','Wilson', 'admin', 'admin')

#print('Admin: ', systemadmin.firstname, systemadmin.lastname, systemadmin.username, systemadmin.password, systemadmin.registrationdate, systemadmin.consultants, systemadmin.members)

systemadmin.updatePassword('newpassword')

consultant = Consultant('Test','Consultant', 'consultant', 'password')
consultant1 = Consultant('Test1','Consultant', 'consultant1', 'password')
consultant2 = Consultant('Test2','Consultant', 'consultant2', 'password')

systemadmin.addConsultant(consultant)
systemadmin.addConsultant(consultant1)
systemadmin.addConsultant(consultant2)

systemadmin.checkUsers()

systemadmin.deleteConsultant(consultant1)

systemadmin.resetConsultantPassword('newpassword', consultant2)

consultant3 = Consultant('Test3','Consultant3', 'consultant', 'password')
systemadmin.updateConsultant(consultant3)

member = Member('Roderick','Wilson', 30, 'M', 61.4, 'Streetname housenumber zipcode City', 'email@hotmail.com', +31612345678, 'username', 'password')
member1 = Member('Test1','Member', 30, 'M', 61.4, 'Streetname housenumber zipcode City', 'email@hotmail.com', +31612345678, 'username1', 'password')
member2 = Member('Test2','Member', 30, 'M', 61.4, 'Streetname housenumber zipcode City', 'email@hotmail.com', +31612345678, 'username2', 'password')

systemadmin.addMember(member)
systemadmin.addMember(member1)
systemadmin.addMember(member2)

systemadmin.checkUsers()

systemadmin.deleteMember(member1)

systemadmin.resetMemberPassword('newpassword', member2)

member3 = Member('Test3','Member3', 30, 'M', 61.4, 'Streetname housenumber zipcode City', 'email3@hotmail.com', +31633333333, 'username2', 'password')
systemadmin.updateMember(member3)

systemadmin.searchMember('username2')

logViewer()

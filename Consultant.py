#consultants and system admins should have profiles, in addition to their usernames and passwords.
#Their profiles contain only first name, last name, and registration date.
from datetime import date

from Members import Member


class Consultant:
    members = list()
    def __init__(self, firstname, lastname, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.registrationdate = date.today()
        self.username = username
        self.password = password

    def updatePassword(self, newpassword):
        print('\nUpdating password')
        self.password = newpassword
        print(self.password)
    
    def addMember(self, member):
        print('\nAdd Member')
        self.members.append(member)
        print(member.firstname, member.lastname)

    def updateMember(self, member):
        for mem in self.members:
            if mem.username == member.username:
                print(f'\nUpdating Member {mem.firstname} to {member.firstname}')
                mem.firstname = member.firstname
                mem.lastname = member.lastname
                mem.age = member.age
                mem.gender = member.gender
                mem.weight = member.weight
                mem.adress = member.adress
                mem.email = member.email
                mem.mobile = member.mobile
        self.checkUsers()
    
    def searchMember(self, memberusername):
        print(f'\nSearching member with username: {memberusername}')
        for mem in self.members:
            if mem.username == memberusername:
                print(mem.ID, mem.firstname, mem.lastname, mem.username, mem.password, mem.registrationdate, mem.age, mem.gender, mem.weight, mem.adress, mem.mobile)

    def checkUsers(self):
        print('\nChecking users')
        print('\nMembers')
        for member in self.members:
            print(member.firstname, member.lastname, member.username, member.password, type(member))

consultant = Consultant('Rode','Willy', 'consultant', 'password')
print('Consultant: ', consultant.firstname, consultant.lastname, consultant.username, consultant.password, consultant.registrationdate)

consultant.updatePassword('newpassword')

member = Member('Roderick','Wilson', 30, 'M', 61.4, 'Streetname housenumber zipcode City', 'email@hotmail.com', +31612345678, 'username', 'password')
member1 = Member('Test1','Member', 30, 'M', 61.4, 'Streetname housenumber zipcode City', 'email@hotmail.com', +31612345678, 'username1', 'password')
member2 = Member('Test2','Member', 30, 'M', 61.4, 'Streetname housenumber zipcode City', 'email@hotmail.com', +31612345678, 'username2', 'password')

consultant.addMember(member)
consultant.addMember(member1)
consultant.addMember(member2)

consultant.checkUsers()

member3 = Member('Test3','Member3', 30, 'M', 61.4, 'Streetname housenumber zipcode City', 'email3@hotmail.com', +31633333333, 'username2', 'password')
consultant.updateMember(member3)

consultant.searchMember('username2')

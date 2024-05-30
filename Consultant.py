#consultants and system admins should have profiles, in addition to their usernames and passwords.
#Their profiles contain only first name, last name, and registration date.
from datetime import date

from Members import Member
from UserServices import UserServices


class Consultant:
    members = list()
    services = UserServices()
    def __init__(self, firstname, lastname, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.registrationdate = date.today()
        self.username = username
        self.password = password

    

consultant = Consultant('Rode','Willy', 'consultant', 'password')
print('Consultant: ', consultant.firstname, consultant.lastname, consultant.username, consultant.password, consultant.registrationdate)

consultant.services.updatePassword(consultant,'newpassword')

member = Member('Roderick','Wilson', 30, 'M', 61.4, 'Streetname housenumber zipcode City', 'email@hotmail.com', +31612345678, 'username', 'password')
member1 = Member('Test1','Member', 30, 'M', 61.4, 'Streetname housenumber zipcode City', 'email@hotmail.com', +31612345678, 'username1', 'password')
member2 = Member('Test2','Member', 30, 'M', 61.4, 'Streetname housenumber zipcode City', 'email@hotmail.com', +31612345678, 'username2', 'password')

consultant.services.addMember(member)
consultant.services.addMember(member1)
consultant.services.addMember(member2)

consultant.services.checkUsers()

member3 = Member('Test3','Member3', 30, 'M', 61.4, 'Streetname housenumber zipcode City', 'email3@hotmail.com', +31633333333, 'username2', 'password')
consultant.services.updateMember(member3)

consultant.services.searchMember('username2')

#consultants and system admins should have profiles, in addition to their usernames and passwords.
#Their profiles contain only first name, last name, and registration date.
from datetime import date
from Consultant import Consultant
from Logger import log,logViewer
from Members import Member
from UserServices import UserServices

"""
● To make a backup of the system and restore a backup (members information and users’ data).

"""

class SystemAdmin:
    consultants = list()
    members = list()
    services = UserServices()
    def __init__(self, firstname, lastname, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.registrationdate = date.today()
        self.username = username
        self.password = password
        log(f'Created SystemAdmin: {self.firstname} {self.lastname} with username: {self.username}')
    
    

# systemadmin = SystemAdmin('Roderick','Wilson', 'admin', 'admin')

# #print('Admin: ', systemadmin.firstname, systemadmin.lastname, systemadmin.username, systemadmin.password, systemadmin.registrationdate, systemadmin.consultants, systemadmin.members)

# systemadmin.services.updatePassword(systemadmin,'newpassword')

# consultant = Consultant('Test','Consultant', 'consultant', 'password')
# consultant1 = Consultant('Test1','Consultant', 'consultant1', 'password')
# consultant2 = Consultant('Test2','Consultant', 'consultant2', 'password')

# systemadmin.services.addConsultant(consultant)
# systemadmin.services.addConsultant(consultant1)
# systemadmin.services.addConsultant(consultant2)

# systemadmin.services.checkUsers()

# systemadmin.services.deleteConsultant(consultant1)

# systemadmin.services.resetConsultantPassword('newpassword', consultant2)

# consultant3 = Consultant('Test3','Consultant3', 'consultant', 'password')
# systemadmin.services.updateConsultant(consultant3)

# member = Member('Roderick','Wilson', 30, 'M', 61.4, 'Streetname housenumber zipcode City', 'email@hotmail.com', +31612345678, 'username', 'password')
# member1 = Member('Test1','Member', 30, 'M', 61.4, 'Streetname housenumber zipcode City', 'email@hotmail.com', +31612345678, 'username1', 'password')
# member2 = Member('Test2','Member', 30, 'M', 61.4, 'Streetname housenumber zipcode City', 'email@hotmail.com', +31612345678, 'username2', 'password')

# systemadmin.services.addMember(member)
# systemadmin.services.addMember(member1)
# systemadmin.services.addMember(member2)

# systemadmin.services.checkUsers()

# systemadmin.services.deleteMember(member1)

# systemadmin.services.resetMemberPassword('newpassword', member2)

# member3 = Member('Test3','Member3', 30, 'M', 61.4, 'Streetname housenumber zipcode City', 'email3@hotmail.com', +31633333333, 'username2', 'password')
# systemadmin.services.updateMember(member3)

# systemadmin.services.searchMember('username2')

#logViewer()

from datetime import date
from Logger import log
from UserServices import UserServices


class User:
    consultants = list()
    members = list()
    services = UserServices()
    def __init__(self, *args):
        if(len(args) > 2):
            self.firstname = args[0]
            self.lastname = args[1]
            self.registrationdate = date.today()
            self.username = args[2]
            self.password = args[3]
            typeUser = self.__class__.__name__
            log(f'Created {typeUser}: {self.firstname} {self.lastname} with username: {self.username}')

class SystemAdmin(User):
    pass

class Consultant(User):
    pass

class SuperAdmin:
    username = 'super_admin'
    password = 'Admin_123?'



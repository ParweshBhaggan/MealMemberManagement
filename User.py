from datetime import date
from Logger import log
from UserServices import UserServices


class User:
    consultants = list()
    members = list()
    def __init__(self, *args):
        if(len(args) > 2):
            self.firstname = args[0]
            self.lastname = args[1]
            self.username = args[2]
            self.password = args[3]
            self.registrationdate = date.today()
        self.services = UserServices(self)
        self.typeUser = self.__class__.__name__
            # log("Changethis", f'New {typeUser} user is created', f'username: {self.username}')

class SystemAdmin(User):
    pass

class Consultant(User):
    pass

class SuperAdmin(User):
    username = 'super_admin'
    password = 'Admin_123?'



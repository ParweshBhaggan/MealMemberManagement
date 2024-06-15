from datetime import date
from Logger import log
from UserServices import UserServices


class User:
    '''The class model of User'''
    def __init__(self, *args):
        if(len(args) > 2):
            self.firstname = args[0]
            self.lastname = args[1]
            self.username = args[2]
            self.password = args[3]
            self.registrationdate = date.today()
        self.services = UserServices(self)
        self.typeUser = self.__class__.__name__

class SystemAdmin(User):
    '''The class model of System Admin'''
    pass

class Consultant(User):
    '''The class model of Consultant'''
    pass

class SuperAdmin(User):
    '''The class model of Super Admin'''
    username = 'super_admin'
    password = 'Admin_123?'



from datetime import date
from Logger import log
from UserServices import UserServices


class User:
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
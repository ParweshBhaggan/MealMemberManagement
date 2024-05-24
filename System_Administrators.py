#consultants and system admins should have profiles, in addition to their usernames and passwords.
#Their profiles contain only first name, last name, and registration date.
from datetime import date


class SystemAdmin:
    def __init__(self, firstname, lastname, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.registrationdate = date.today()
        self.username = username
        self.password = password

systemadmin = SystemAdmin('Roderick','Wilson', 'admin', 'admin')

print(systemadmin.firstname, systemadmin.lastname, systemadmin.username, systemadmin.password, systemadmin.registrationdate)


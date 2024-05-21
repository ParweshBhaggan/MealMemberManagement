#consultants and system admins should have profiles, in addition to their usernames and passwords.
#Their profiles contain only first name, last name, and registration date.
from datetime import date


class Consultant:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.registrationdate = date.today()
        self.username = firstname + ' ' + lastname
        self.password = 1234

consultant = Consultant('Rode','Willy')

print(consultant.firstname, consultant.lastname, consultant.username, consultant.password, consultant.registrationdate)
#consultants and system admins should have profiles, in addition to their usernames and passwords.
#Their profiles contain only first name, last name, and registration date.
from datetime import date


class Consultant:
    def __init__(self, firstname, lastname, username, password):
        self.firstname = firstname
        self.lastname = lastname
        self.registrationdate = date.today()
        self.username = username
        self.password = password

consultant = Consultant('Rode','Willy', 'username', 'password')

print(consultant.firstname, consultant.lastname, consultant.username, consultant.password, consultant.registrationdate)
"""First Name and Last Name

● Age, Gender, Weight

● Address (Street name, House number, Zip Code (DDDDXX),

 City (system should generate a list of 10 city names of your choice predefined in the system)

● Email Address

● Mobile Phone (+31-6-DDDDDDDD) – only DDDDDDDD to be entered by the user.

"""

from datetime import date


class Member:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
        self.registrationdate = date.today()
        self.age = 30
        self.gender = 'M'
        self.weight = 50.23
        self.adress = 'Verlengde singelstraat 01 2613EW'
        self.city = ['AMS', 'DELFT', 'ROTT', 'DENHAAG']
        self.email = firstname + lastname + '@hotmail.com'
        self.mobile = +31612615703
        self.username = firstname + ' ' + lastname
        self.password = 1234

member = Member('Roderick','Wilson')

print(member.firstname, member.lastname, member.username, member.password, member.registrationdate, member.age, member.adress, member.city[1], member.mobile)
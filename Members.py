"""First Name and Last Name

● Age, Gender, Weight

● Address (Street name, House number, Zip Code (DDDDXX),

 City (system should generate a list of 10 city names of your choice predefined in the system)

● Email Address

● Mobile Phone (+31-6-DDDDDDDD) – only DDDDDDDD to be entered by the user.

"""

from datetime import date

import Unique_Generator # type: ignore


class Member:
    def __init__(self, firstname, lastname, age, gender, weight, adress, city, email, mobile, username, password):
        self.ID = Unique_Generator.generate()
        self.firstname = firstname
        self.lastname = lastname
        self.registrationdate = date.today()
        self.age = age
        self.gender = gender
        self.weight = weight
        self.adress = adress
        self.email = email
        self.mobile = mobile
        self.username = username
        self.password = password

member = Member('Roderick','Wilson', 30, 'M', 61.4, 'Streetname housenumber zipcode City', 'email@hotmail.com', +31612345678, 'username', 'password')

print(member.ID, member.firstname, member.lastname, member.username, member.password, member.registrationdate, member.age, member.gender, member.weight, member.adress, member.mobile)
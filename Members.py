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
    def __init__(self, firstname, lastname, age, gender, weight, adress, email, mobile, username, password):
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

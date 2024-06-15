from datetime import date
import Unique_Generator 


class Member:
    '''Class model of Member'''
    
    def __init__(self, firstname, lastname, age, gender, weight, adress, email, mobile):
        self.membershipID = Unique_Generator.generate()
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender
        self.weight = weight
        self.adress = adress
        self.email = email
        self.mobile = mobile
        self.registrationdate = date.today()
       
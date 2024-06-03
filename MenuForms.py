from User import*
from Members import Member
from rodeDatabase import createConsultant, createSystemAdmin


class MenuForms:
    def __init__(self) -> None:
        pass

    def UserForm(self, user):
        firstname = input("Enter Firstname: \n")
        lastname = input("Enter Lastname: \n")
        username = input("Enter Username: \n")
        password = input("Enter Password: \n")
        
        name = user.__class__.__name__
        if(name == "SystemAdmin"):
            user = SystemAdmin(firstname, lastname, username, password)
            createSystemAdmin(user)
        elif(name == "Consultant"):
            user = Consultant(firstname, lastname, username, password)
            createConsultant(user)
            
        print(user.__class__.__name__)

        


    def MemberForm(self, member):
        firstname = input("Enter Firstname: \n")
        lastname = input("Enter Lastname: \n")
        age = int(input("Enter Age: \n"))
        gender = input("Enter Gender: \n")
        weight = float(input("Enter Weight: \n"))
        address = input("Enter Address: \n")
        email = input("Enter Email: \n")
        mobile = input("Enter Mobile: \n")

        member = Member(firstname, lastname, age, gender, weight, address, email, mobile)
        
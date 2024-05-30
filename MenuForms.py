from Members import Member


class MenuForms:
    def __init__(self) -> None:
        pass

    def UserForm(self, user):
        firstname = input("Enter Firstname: \n")
        lastname = input("Enter Lastname: \n")
        username = input("Enter Username: \n")
        password = input("Enter Password: \n")

        


    def MemberForm(self, member):
        firstname = input("Enter Firstname: \n")
        lastname = input("Enter Lastname: \n")
        age = int(input("Enter Age: \n"))
        gender = input("Enter Gender: \n")
        weight = float(input("Enter Weight: \n"))
        address = input("Enter Address: \n")
        email = input("Enter Email: \n")
        mobile = input("Enter Mobile: \n")
        username = input("Enter Username: \n")
        password = input("Enter Password: \n")

        member = Member(firstname, lastname, age, gender, weight, address, email, mobile, username, password)
        
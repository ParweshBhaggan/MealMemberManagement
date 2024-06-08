
from User import Consultant, SuperAdmin, SystemAdmin
from Members import Member
import random

class MenuForms:
    def __init__(self) -> None:
        self.adressform = AddressForm()

    def UserForm(self, user):
        firstname = input("Enter Firstname: \n")
        lastname = input("Enter Lastname: \n")
        username = input("Enter Username: \n")
        password = input("Enter Password: \n")
        
        name = user.__class__.__name__
        if(name == "SystemAdmin"):
            user = SystemAdmin(firstname, lastname, username, password)
        elif(name == "Consultant"):
            user = Consultant(firstname, lastname, username, password)
        return user

    def MemberForm(self):
        firstname = input("Enter Firstname: \n")
        lastname = input("Enter Lastname: \n")
        age = int(input("Enter Age: \n"))
        gender = input("Enter Gender: \n")
        weight = float(input("Enter Weight: \n"))
        address = self.adressform.GetAdress()
        email = input("Enter Email: \n")
        mobile = input("Enter Mobile: \n")

        member = Member(firstname, lastname, age, gender, weight, address, email, mobile)
        return member
        
    def SearchTermForm(self):
        search_type = input("Enter search term: \n")
        
        if search_type == '':
            print("Invalid search type.")
            self.SearchTermForm()
        return search_type
    
    def SelectUserForm(self, listUser):
        print("===================================")
        print("Found users: ")
        if len(listUser) > 0:
            menuItem = 1
            for index in range(0, len(listUser)):
                if hasattr(listUser[index], 'username'):
                    print(f"{menuItem} {listUser[index].username}" )
                else:
                    print(f"{menuItem} {listUser[index].firstname} {listUser[index].lastname}" )
                menuItem +=1
            print("=================================")
            selectedOption = int(input("Select user: "))
            
            if selectedOption < menuItem:
                
                selectedIndex = selectedOption - 1
                selectedUser = listUser[selectedIndex]
                print( "U have selected: "  + selectedUser.firstname)
                print("=================================")
                return selectedUser
            else:
                print("=====================")
                print("Wrong option! Retry!")
                self.SelectUserForm(listUser)
    
    def DeleteUserForm(self, user):
        if hasattr(user, 'typeUser'):
            print(f"Are you sure you want to delete the {user.typeUser}: {user.username}? (y/n)")
        else:
            print(f"Are you sure you want to delete the Member: {user.firstname} {user.lastname}? (y/n)")
        confirm = input()
        if confirm.lower() == 'y':
            print("Deleting user...")
            return True
        else:
            print("User deletion cancelled.")
            return False
    
    def ResetConsultantForm(self, consultant):
        print("Reset Consultant Password")
        password = input(f"Enter new Password for '{consultant.username}': \n")
        consultant.password = password
        return consultant
    
    def ResetAdminForm(self, admin):
        print("Reset Admin Password")
        password = input(f"Enter new Password for '{admin.username}': \n")
        admin.password = password
        return admin
    
    def UpdateAdminForm(self, admin):
        print("Update Admin Information")
        firstname = input(f"Enter Firstname (or enter to skip): \n") or admin.firstname
        lastname = input(f"Enter Lastname (or enter to skip): \n") or admin.lastname
        username = input(f"Enter Username (or enter to skip): \n") or admin.username

        admin.firstname = firstname
        admin.lastname = lastname
        admin.username = username
        admin.password = admin.password

        return admin
    
    def UpdateConsultantForm(self, consultant):
        print("Update Consultant Information")
        firstname = input(f"Enter Firstname (or enter to skip): \n") or consultant.firstname
        lastname = input(f"Enter Lastname (or enter to skip): \n") or consultant.lastname
        username = input(f"Enter Username (or enter to skip): \n") or consultant.username

        consultant.firstname = firstname
        consultant.lastname = lastname
        consultant.username = username
        consultant.password = consultant.password

        return consultant
    
    def UpdateMemberForm(self, member):
        print("Update Member Information")
        firstname = input(f"Enter Firstname (or enter to skip): \n") or member.firstname
        lastname = input(f"Enter Lastname (or enter to skip): \n") or member.lastname
        age = input(f"Enter Age (or enter to skip): \n") or member.age
        gender = input(f"Enter Gender (or enter to skip): \n") or member.gender
        weight = input(f"Enter Weight (or enter to skip): \n") or member.weight
        adress = self.adressform.UpdateAdress(member.adress)
        email = input(f"Enter Email (or enter to skip): \n") or member.email
        mobile = input(f"Enter Mobile (or enter to skip): \n") or member.mobile

        member.firstname = firstname
        member.lastname = lastname
        member.age = int(age)
        member.gender = gender
        member.weight = float(weight)
        member.adress = adress
        member.email = email
        member.mobile = mobile

        return member
    
    def UpdatePasswordForm(self):
        newPassword = input("Enter new password: \n")
        return newPassword
    
    

class AddressForm:
    def __init__(self):
        self.cities = ["Amsterdam", "Rotterdam", "Utrecht", "Eindhoven", "Groningen", "Tilburg", "Almere", "Breda", "Nijmegen", "Haarlem"]

    def DisplayCities(self):
        print("Select a city from the list below:")
        for index, city in enumerate(self.cities, start=1):
            print(f"{index}. {city}")

    def SelectCity(self):
        while True:
            try:
                choice = int(input("Enter the number corresponding to your city: "))
                if 1 <= choice <= len(self.cities):
                    return self.cities[choice - 1]
                else:
                    print(f"Please select a number between 1 and {len(self.cities)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

    def GetAdress(self):
        streetname = input("Enter Street Name: ")
        housenumber = input("Enter House Number: ")
        while True:
            zipcode = input("Enter Zip Code (DDDDXX): ")
            if len(zipcode) == 6 and zipcode[:4].isdigit() and zipcode[4:].isalpha():
                break
            else:
                print("Invalid Zip Code format. Please enter in the format DDDDXX.")

        self.DisplayCities()
        city = self.SelectCity()

        address = f"{streetname} {housenumber}, {zipcode} {city}"
        return address
    
    def UpdateAdress(self, memberadress):
        streetname = input("Enter Street Name (or press Enter to skip): ")
        if not streetname:
            return memberadress

        housenumber = input("Enter House Number (or press Enter to skip): ")
        if not housenumber:
            return memberadress

        while True:
            zipcode = input("Enter Zip Code (DDDDXX) (or press Enter to skip): ")
            if not zipcode:
                return memberadress
            if len(zipcode) == 6 and zipcode[:4].isdigit() and zipcode[4:].isalpha():
                break
            else:
                print("Invalid Zip Code format. Please enter in the format DDDDXX.")

        self.DisplayCities()
        city = self.UpdateCity()
        if not city:
            return memberadress

        return f"{streetname} {housenumber}, {zipcode} {city}"
    
    def UpdateCity(self):
        while True:
            choice = input("Enter the number corresponding to your city (or press Enter to skip): ")
            if not choice:
                return None
            try:
                choice = int(choice)
                if 1 <= choice <= len(self.cities):
                    return self.cities[choice - 1]
                else:
                    print(f"Please select a number between 1 and {len(self.cities)}.")
            except ValueError:
                print("Invalid input. Please enter a number.")

# def main():
#     address_form = AddressForm()
#     address = address_form.get_address()
#     print("\nAddress Entered:")
#     print(f"Street Name: {address['street_name']}")
#     print(f"House Number: {address['house_number']}")
#     print(f"Zip Code: {address['zip_code']}")
#     print(f"City: {address['city']}")

# if __name__ == "__main__":
#     main()

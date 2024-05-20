class SuperAdmin:
    __instance = None
    username = "super_admin"
    password = "Admin_123?"

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super(SuperAdmin, cls).__new__(cls)
        return cls.__instance

    @staticmethod
    def verify_credentials(username, password):
        return username == SuperAdmin.username and password == SuperAdmin.password

# Usage example
if __name__ == "__main__":
    # Creating the singleton instance
    super_admin1 = SuperAdmin()

    # Verifying credentials
    if super_admin1.verify_credentials("super_admin", "Admin_123?"):
        print("Credentials verified.")
    else:
        print("Invalid credentials.")

    # Attempting to create another instance
    super_admin2 = SuperAdmin()

    # Checking if both instances are the same
    print(f"super_admin1 is super_admin2: {super_admin1 is super_admin2}")

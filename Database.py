import sqlite3
from Members import Member
from Encryption import EncryptionHandler, HashHandler
class  DatabaseManager:
    '''This class handles database actions.'''
    dbname = "MealMemberManagement.db" 

    def __init__(self):
        
        self.con = sqlite3.connect(self.dbname)
        self.security = EncryptionHandler()
        self.hash_handler = HashHandler()
        self.cur = self.con.cursor()
        self.CreateMemberTable()
        self.CreateSystemAdminTable()
        self.CreateConsultantTable()
        self.con.commit()
        self.con.close()

################################################################################################
# TABLES here below 
    def CreateMemberTable(self):
        '''Creates table: Member.'''
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS Member(
            membershipID VARCHAR(255) PRIMARY KEY NOT NULL,
            firstname VARCHAR(255) NOT NULL,
            lastname VARCHAR(255) NOT NULL,
            age INT NOT NULL,
            gender VARCHAR(50) NOT NULL,
            weight DECIMAL(5, 2) NOT NULL,
            adress TEXT NOT NULL,
            email VARCHAR(255) NOT NULL UNIQUE,
            mobile VARCHAR(20) NOT NULL UNIQUE,
            registrationdate DATE NOT NULL
        )
    """)

    def CreateSystemAdminTable(self):
        '''Creates table: System Admin.'''

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS SystemAdmin(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            firstname VARCHAR(255) NOT NULL,
            lastname VARCHAR(255) NOT NULL,
            username VARCHAR(255) UNIQUE,
            password VARCHAR(255) NOT NULL,
            userpassword VARCHAR(255) NOT NULL,
            temp_pass INTEGER NOT NULL,
            registrationdate DATE NOT NULL
        )
    """)

    def CreateConsultantTable(self):
        '''Creates table: Consult.'''

        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS Consultant (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            firstname VARCHAR(255) NOT NULL,
            lastname VARCHAR(255) NOT NULL,
            username VARCHAR(255) UNIQUE,
            password VARCHAR(255) NOT NULL,
            userpassword VARCHAR(255) NOT NULL,
            temp_pass INTEGER NOT NULL,
            registrationdate DATE NOT NULL
        )
    """)

################################################################################################
# LOGIN here below 
    def loginUser(self, username, password):
        
        '''Login from the database.'''
        from User import Consultant, SuperAdmin, SystemAdmin

        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()

        if username == "super_admin" and password == "Admin_123?":
            con.close()
            loggedInUser = SuperAdmin()
            return True, loggedInUser
        passwordSafety = username+password
        passwordSafety = self.hash_handler.hash_password(passwordSafety)
        #self.cur.execute("SELECT * FROM SystemAdmin WHERE username = ? AND password = ?", (username, password))
        self.cur.execute("SELECT * FROM SystemAdmin WHERE userpassword = ?", (passwordSafety,))
        user = self.cur.fetchone()

        if user:
            loggedInUser = SystemAdmin(self.security.decrypt_data(user[1]), self.security.decrypt_data(user[2]), self.security.decrypt_data(user[3]), password)
            loggedInUser.id = user[0]
            loggedInUser.temp_pass = user[6]
            loggedInUser.registrationdate = self.security.decrypt_data(user[7])
            
            con.close()
            return True, loggedInUser

        self.cur.execute("SELECT * FROM Consultant WHERE userpassword = ?", (passwordSafety,))
        user = self.cur.fetchone()

        con.close()

        if user:
            loggedInUser = Consultant(self.security.decrypt_data(user[1]), self.security.decrypt_data(user[2]), self.security.decrypt_data(user[3]), password)
            loggedInUser.id = user[0]
            loggedInUser.temp_pass = user[6]
            loggedInUser.registrationdate = self.security.decrypt_data(user[7])
            return True, loggedInUser
        else:
            return False, None

################################################################################################
# CREATE here below   
    def createMember(self, member):
        '''Insert Data: Member.'''
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        # Encrypt sensitive data
        encrypted_ID = self.security.encrypt_data(str(member.membershipID))
        encrypted_firstname = self.security.encrypt_data(member.firstname)
        encrypted_lastname = self.security.encrypt_data(member.lastname)
        encrypted_registrationdate = self.security.encrypt_data(str(member.registrationdate))
        encrypted_age = self.security.encrypt_data(member.age)
        encrypted_gender = self.security.encrypt_data(member.gender)
        encrypted_adress = self.security.encrypt_data(member.adress)
        encrypted_email = self.security.encrypt_data(member.email)
        encrypted_weight = self.security.encrypt_data(member.weight)
        encrypted_mobile = self.security.encrypt_data(member.mobile)
        
        self.cur.execute("""
            INSERT INTO Member (membershipID, firstname, lastname, registrationdate, age, gender, weight, adress, email, mobile)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (encrypted_ID, encrypted_firstname,  encrypted_lastname , encrypted_registrationdate, encrypted_age,  encrypted_gender, encrypted_weight, encrypted_adress, encrypted_email,  encrypted_mobile))
        con.commit()
        con.close()

    def createConsultant(self,user):
        '''Insert Data: Consult.'''
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        # Encrypt sensitive data
        encrypted_firstname = self.security.encrypt_data(user.firstname)
        encrypted_lastname = self.security.encrypt_data(user.lastname)
        encrypted_username = self.security.encrypt_data(user.username)
        encrypted_password = self.security.encrypt_data(user.password)
        encrypted_registrationdate = self.security.encrypt_data(str(user.registrationdate))
        
        # Hash the password
        passwordSafety = user.username + user.password
        hashed_password = self.hash_handler.hash_password(passwordSafety)
        self.cur.execute("""
            INSERT INTO Consultant (firstname, lastname, username, password,  userpassword, temp_pass, registrationdate)
            VALUES (?, ?, ?, ?, ?, ?, ?);
        """, (encrypted_firstname, encrypted_lastname, encrypted_username, encrypted_password, hashed_password, user.temp_pass, encrypted_registrationdate))

        con.commit()
        con.close()

    def createSystemAdmin(self,user):
        '''Insert Data: System Admin.'''
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        # Encrypt sensitive data
        encrypted_firstname = self.security.encrypt_data(user.firstname)
        encrypted_lastname = self.security.encrypt_data(user.lastname)
        encrypted_username = self.security.encrypt_data(user.username)
        encrypted_password = self.security.encrypt_data(user.password)
        encrypted_registrationdate = self.security.encrypt_data(str(user.registrationdate))
        
        # Hash the password
        passwordSafety = user.username + user.password
        hashed_password = self.hash_handler.hash_password(passwordSafety)
        self.cur.execute("""
            INSERT INTO SystemAdmin (firstname, lastname, username, password, userpassword, temp_pass, registrationdate)
            VALUES (?, ?, ?, ?, ?, ?, ?);
        """, (encrypted_firstname, encrypted_lastname , encrypted_username, encrypted_password ,hashed_password, user.temp_pass, encrypted_registrationdate))
        con.commit()
        con.close()

################################################################################################
# UPDATE here below 
    def updateMember(self, member):
        '''Update Data: Member.'''
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        # Encrypt sensitive data
        encrypted_firstname = self.security.encrypt_data(member.firstname)
        encrypted_lastname = self.security.encrypt_data(member.lastname)
        encrypted_age = self.security.encrypt_data(str(member.age))
        encrypted_gender = self.security.encrypt_data(member.gender)
        encrypted_adress = self.security.encrypt_data(member.adress)
        encrypted_email = self.security.encrypt_data(member.email)
        encrypted_weight = self.security.encrypt_data(str(member.weight))
        encrypted_mobile = self.security.encrypt_data(member.mobile)
        self.cur.execute("""
            UPDATE Member
            SET firstname = ?, lastname = ?, age = ?, gender = ?, weight = ?, adress = ?, email = ?, mobile = ?
            WHERE membershipID = ?;
        """, (encrypted_firstname,  encrypted_lastname, encrypted_age,  encrypted_gender, encrypted_weight, encrypted_adress, encrypted_email,  encrypted_mobile, member.membershipID))
        con.commit()
        con.close()

    def updateConsultant(self, user, id):
        '''Update Data: Consultant.'''
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
           # Encrypt sensitive data
        passwordSafety = user.username + user.password
        hashed_password = self.hash_handler.hash_password(passwordSafety)
        encrypted_firstname = self.security.encrypt_data(user.firstname)
        encrypted_lastname = self.security.encrypt_data(user.lastname)
        encrypted_username = self.security.encrypt_data(user.username)
        
        self.cur.execute("""
            UPDATE Consultant
            SET firstname = ?, lastname = ?, username = ?, userpassword = ?
            WHERE id = ?;
        """, (   encrypted_firstname,  encrypted_lastname,  encrypted_username, hashed_password, id))
        con.commit()
        con.close()

    def updateSystemAdmin(self,user, id):
        '''Update Data: System Admin.'''
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        # Encrypt sensitive data
        passwordSafety = user.username + user.password
        hashed_password = self.hash_handler.hash_password(passwordSafety)
        encrypted_firstname = self.security.encrypt_data(user.firstname)
        encrypted_lastname = self.security.encrypt_data(user.lastname)
        encrypted_username = self.security.encrypt_data(user.username)
        self.cur.execute("""
            UPDATE SystemAdmin
            SET firstname = ?, lastname = ?, username = ?, userpassword = ?
            WHERE id = ?;
        """, (encrypted_firstname,  encrypted_lastname, encrypted_username, hashed_password , id))
        con.commit()
        con.close()

################################################################################################
# RESET here below     
    def UpdatePasswordOwnSystemAdmin(self, systemadmin):
        '''Updates own password of System Admin.'''
        
        password = self.security.encrypt_data(systemadmin.password)
        hashed_password = self.hash_handler.hash_password(systemadmin.username + systemadmin.password)
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            UPDATE SystemAdmin
            SET password = ?, userpassword = ?, temp_pass = ?
            WHERE id = ?;
        """, (password, hashed_password, 0, systemadmin.id))
        con.commit()
        con.close()
    
    def UpdatePasswordOwnConsultant(self, consultant):
        '''Updates own password of Consultant.'''
        
        password = self.security.encrypt_data(consultant.password)
        hashed_password = self.hash_handler.hash_password(consultant.username + consultant.password)
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            UPDATE Consultant
            SET password = ?, userpassword = ?, temp_pass = ?
            WHERE id = ?;
        """, (password, hashed_password, 0, consultant.id))
        con.commit()
        con.close()

    def resetConsultantPassword(self, consultant):
        '''Reset password of Consultant.'''
        password = self.security.encrypt_data(consultant.password)
        hashed_password = self.hash_handler.hash_password(consultant.username + consultant.password)
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        self.cur.execute("""
            UPDATE Consultant
            SET password = ?, userpassword = ?, temp_pass = ?
            WHERE id = ?;
        """, (password, hashed_password, 1, consultant.id))
        con.commit()
        con.close()

    def resetSystemAdminPassword(self,systemadmin):
        '''Reset password of System Admin.'''
        
        password = self.security.encrypt_data(systemadmin.password)
        hashed_password = self.hash_handler.hash_password(systemadmin.username + systemadmin.password)
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            UPDATE SystemAdmin
            SET password = ?, userpassword = ?, temp_pass = ?
            WHERE id = ?;
        """, (password, hashed_password, 1, systemadmin.id))
        con.commit()
        con.close()

################################################################################################
# DELETE here below
    def deleteMember(self, member):
        '''Delete Data: Member.'''
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        self.cur.execute("""
            DELETE FROM Member 
            WHERE membershipID = ?;
        """, (member.membershipID,))
        con.commit()
        con.close()

    def deleteConsultant(self, consultant):
        '''Delete Data: Consultant.'''
       
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        self.cur.execute("""
            DELETE FROM Consultant 
            WHERE id = ?;
        """, (consultant.id,))
        con.commit()
        con.close()


    def deleteSystemAdmin(self,systemadmin):
        '''Delete Data: System Admin.'''
        
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            DELETE FROM SystemAdmin 
            WHERE id = ?;
        """, (systemadmin.id,))
        con.commit()
        con.close()

################################################################################################
# GET here below
    def getallUsers(self):
        '''Get all Users from the database.'''
        from User import SystemAdmin,Consultant
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        self.cur.execute("""
            SELECT * FROM SystemAdmin;
        """)
        listAdmins = self.cur.fetchall()
        self.cur.execute("""
            SELECT * FROM Consultant;
        """)
        listCons = self.cur.fetchall()
        listUsers = []

    
        for res in listAdmins:
            decrypted_firstname = self.security.decrypt_data(res[1])
            decrypted_lastname = self.security.decrypt_data(res[2])
            decrypted_username = self.security.decrypt_data(res[3])
            decrypted_password = self.security.decrypt_data(res[4])
            decrypted_registrationdate = self.security.decrypt_data(res[7])
            
            systemAdmin = SystemAdmin(decrypted_firstname, decrypted_lastname, decrypted_username, decrypted_password)
            systemAdmin.registrationdate = decrypted_registrationdate
            systemAdmin.id = res[0]
            listUsers.append(systemAdmin)
            
        for res in listCons:
            decrypted_firstname = self.security.decrypt_data(res[1])
            decrypted_lastname = self.security.decrypt_data(res[2])
            decrypted_username = self.security.decrypt_data(res[3])
            decrypted_password = self.security.decrypt_data(res[4])
            decrypted_registrationdate = self.security.decrypt_data(res[7])
            
            
            consultant = Consultant(decrypted_firstname, decrypted_lastname, decrypted_username, decrypted_password)
            consultant.registrationdate = decrypted_registrationdate
            consultant.id = res[0]

            listUsers.append(consultant)
        

        con.close()
        return listUsers

    def getallMembers(self):
        '''Get all Members from the database.'''
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        self.cur.execute("""
            SELECT * FROM Member;
        """)
        listMems = self.cur.fetchall()
        listUsers = []
        for mem in listMems:
            decrypted_ID = self.security.decrypt_data(mem[0])
            decrypted_firstname = self.security.decrypt_data(mem[1])
            decrypted_lastname = self.security.decrypt_data(mem[2])
            decrypted_age = self.security.decrypt_data(mem[3])
            decrypted_gender = self.security.decrypt_data(mem[4])
            decrypted_weight = self.security.decrypt_data(mem[5])
            decrypted_address = self.security.decrypt_data(mem[6])
            decrypted_email = self.security.decrypt_data(mem[7])
            decrypted_mobile = self.security.decrypt_data(mem[8])
            
            member = Member(decrypted_firstname, decrypted_lastname, decrypted_age, decrypted_gender, decrypted_weight, decrypted_address, decrypted_email, decrypted_mobile, decrypted_ID)
            member.membershipID = mem[0]
            listUsers.append(member)
        con.close()
        return listUsers

################################################################################################
# FETCHES here below
    def FetchMemberMobile(self, mobileNumber):
        '''Get specific Mobile data of Member from the database.'''
        allmembers = self.getallMembers()
        for member in allmembers:
            if member.mobile == mobileNumber:
                return member.mobile
        return None
    
    def FetchMemberEmail(self, email):
        '''Get specific Email data of Member from the database.'''
        allmembers = self.getallMembers()
        for member in allmembers:
            if member.email.lower() == email.lower():
                return member.email
        return None
    
    def FetchConsUsername(self, consusername):
        '''Get specific Username data of Consultant from the database.'''
        allusers = self.getallUsers()
        for user in allusers:
            if user.typeUser == "Consultant":
                if user.username.lower() == consusername.lower():
                    return user.username
        return None
    
    def FetchConsultantID(self, user):
        '''Get specific ID data of Consultant from the database.'''
        username = ""
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            SELECT id FROM Consultant
            WHERE username = ?;
        """, (username,))
        id = self.cur.fetchone()[0]
        con.commit()
        con.close()
        return id
    
    def FetchSystemAdminID(self, user):
        '''Get specific ID data of SystemAdmin from the database.'''
        username = self.security.encrypt_data(user.username)
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            SELECT id FROM SystemAdmin
            WHERE username = ?;
        """, (username,))
        id = self.cur.fetchone()[0]
        con.commit()
        con.close()
        return id
    
    def FetchAdminUsername(self, adminusername):
        '''Get specific Username data of System Admin from the database.'''
        allusers = self.getallUsers()
        for user in allusers:
            if user.typeUser == "SystemAdmin":
                if user.username.lower() == adminusername.lower():
                    return user.username
        return None
import sqlite3
from Members import Member
from Encryption import EncryptionHandler, HashHandler
class  DatabaseManager:
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
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS SystemAdmin(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            firstname VARCHAR(255) NOT NULL,
            lastname VARCHAR(255) NOT NULL,
            username VARCHAR(255) UNIQUE,
            password VARCHAR(255) NOT NULL,
            registrationdate DATE NOT NULL
        )
    """)

    def CreateConsultantTable(self):
        self.cur.execute("""
        CREATE TABLE IF NOT EXISTS Consultant (
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            firstname VARCHAR(255) NOT NULL,
            lastname VARCHAR(255) NOT NULL,
            username VARCHAR(255) UNIQUE,
            password VARCHAR(255) NOT NULL,
            registrationdate DATE NOT NULL
        )
    """)

################################################################################################
# LOGIN here below 
    def loginUser(self, username, password):
        from User import Consultant, SuperAdmin, SystemAdmin

        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()

        if username == "1" and password == "1":# superadmin - Admin_123?
            con.close()
            loggedInUser = SuperAdmin()
            return True, loggedInUser
        username = self.security.encrypt_data(username)
        self.cur.execute("SELECT * FROM SystemAdmin WHERE username = ? AND password = ?", (username, password))
        user = self.cur.fetchone()

        if user:
            loggedInUser = SystemAdmin(self.security.decrypt_data(user[1]), self.security.decrypt_data(user[2]), self.security.decrypt_data(user[3]), self.security.decrypt_data(user[4]))
            loggedInUser.registrationdate = self.security.decrypt_data(user[5])
            
            con.close()
            return True, loggedInUser

        self.cur.execute("SELECT * FROM Consultant WHERE username = ? AND password = ?", (username, password))
        user = self.cur.fetchone()

        con.close()

        if user:
            loggedInUser = Consultant(self.security.decrypt_data(user[1]), self.security.decrypt_data(user[2]), self.security.decrypt_data(user[3]), self.security.decrypt_data(user[4]))
            loggedInUser.registrationdate = self.security.decrypt_data(user[5])
            return True, loggedInUser
        else:
            return False, None

################################################################################################
# CREATE here below   
    def createMember(self, member):
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        self.cur.execute("""
            INSERT INTO Member (membershipID, firstname, lastname, registrationdate, age, gender, weight, adress, email, mobile)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (member.membershipID, member.firstname, member.lastname, member.registrationdate, member.age, member.gender, member.weight, member.adress, member.email, member.mobile))
        con.commit()
        con.close()

    def createConsultant(self,user):
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        self.cur.execute("""
            INSERT INTO Consultant (firstname, lastname, username, password, registrationdate)
            VALUES (?, ?, ?, ?, ?);
        """, (user.firstname, user.lastname, user.username, user.password, user.registrationdate))
        con.commit()
        con.close()

    def createSystemAdmin(self,user):
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        self.cur.execute("""
            INSERT INTO SystemAdmin (firstname, lastname, username, password, registrationdate)
            VALUES (?, ?, ?, ?, ?);
        """, (user.firstname, user.lastname, user.username, user.password, user.registrationdate))
        con.commit()
        con.close()

################################################################################################
# UPDATE here below 
    def updateMember(self, member):
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        self.cur.execute("""
            UPDATE Member
            SET firstname = ?, lastname = ?, age = ?, gender = ?, weight = ?, adress = ?, email = ?, mobile = ?
            WHERE membershipID = ?;
        """, (member.firstname, member.lastname, member.age, member.gender, member.weight, member.adress, member.email, member.mobile, member.membershipID))
        con.commit()
        con.close()

    def updateConsultant(self, user, id):
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        self.cur.execute("""
            UPDATE Consultant
            SET firstname = ?, lastname = ?, username = ?
            WHERE id = ?;
        """, (user.firstname, user.lastname, user.username, id))
        con.commit()
        con.close()

    def updateSystemAdmin(self,user, id):
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            UPDATE SystemAdmin
            SET firstname = ?, lastname = ?, username = ?
            WHERE id = ?;
        """, (user.firstname, user.lastname, user.username, id))
        con.commit()
        con.close()

################################################################################################
# RESET here below     
    def resetPassword(self,newpassword, username):
        name = self.security.encrypt_data(username)
        password = self.hash_handler.hash_password(newpassword)
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            UPDATE SystemAdmin
            SET password = ?
            WHERE username = ?
        """, (password, name))
        con.commit()
        con.close()

    def resetConsultantPassword(self, consultant):
        username = self.security.encrypt_data(consultant.username)
        password = self.hash_handler.hash_password(consultant.password)
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        self.cur.execute("""
            UPDATE Consultant
            SET password = ?
            WHERE username = ?
        """, (password, username))
        con.commit()
        con.close()

    def resetSystemAdminPassword(self,sytemadmin):
        username = self.security.encrypt_data(sytemadmin.username)
        password = self.hash_handler.hash_password(sytemadmin.password)
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            UPDATE SystemAdmin
            SET password = ?
            WHERE username = ?
        """, (password, username))
        con.commit()
        con.close()

################################################################################################
# DELETE here below
    def deleteMember(self, member):
        ID = self.security.encrypt_data(member.membershipID)
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        self.cur.execute("""
            DELETE FROM Member 
            WHERE membershipID = ?;
        """, (ID,))
        con.commit()
        con.close()

    def deleteConsultant(self, consultant):
        username = self.security.encrypt_data(consultant.username)
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        self.cur.execute("""
            DELETE FROM Consultant 
            WHERE username = ?
        """, (username,))
        con.commit()
        con.close()


    def deleteSystemAdmin(self,systemadmin):
        username = self.encrypt_data(systemadmin.username)
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            DELETE FROM SystemAdmin 
            WHERE username = ?
        """, (username,))
        con.commit()
        con.close()

################################################################################################
# GET here below
    def getallUsers(self):
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
            decrypted_registrationdate = self.security.decrypt_data(res[5])
            
            systemAdmin = SystemAdmin(decrypted_firstname, decrypted_lastname, decrypted_username, decrypted_password)
            systemAdmin.registrationdate = decrypted_registrationdate
            listUsers.append(systemAdmin)
        
        for res in listCons:
            decrypted_firstname = self.security.decrypt_data(res[1])
            decrypted_lastname = self.security.decrypt_data(res[2])
            decrypted_username = self.security.decrypt_data(res[3])
            decrypted_password = self.security.decrypt_data(res[4])
            decrypted_registrationdate = self.security.decrypt_data(res[5])
            
            consultant = Consultant(decrypted_firstname, decrypted_lastname, decrypted_username, decrypted_password)
            consultant.registrationdate = decrypted_registrationdate
            listUsers.append(consultant)

        con.close()
        return listUsers

    def getallMembers(self):
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        self.cur.execute("""
            SELECT * FROM Member;
        """)
        listMems = self.cur.fetchall()
        listUsers = []
        for mem in listMems:
            decrypted_membershipID = self.security.decrypt_data(mem[0])
            decrypted_firstname = self.security.decrypt_data(mem[1])
            decrypted_lastname = self.security.decrypt_data(mem[2])
            decrypted_age = self.security.decrypt_data(mem[3])
            decrypted_gender = self.security.decrypt_data(mem[4])
            decrypted_weight = self.security.decrypt_data(mem[5])
            decrypted_address = self.security.decrypt_data(mem[6])
            decrypted_email = self.security.decrypt_data(mem[7])
            decrypted_mobile = self.security.decrypt_data(mem[8])
            
            member = Member(decrypted_firstname, decrypted_lastname, decrypted_age, decrypted_gender, decrypted_weight, decrypted_address, decrypted_email, decrypted_mobile)
            member.membershipID = decrypted_membershipID
            listUsers.append(member)
        con.close()
        return listUsers

################################################################################################
# FETCHES here below
    def FetchMemberMobile(self, mobileNumber):
        mobilenumber = self.encrypt_data(mobileNumber)
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            SELECT mobile FROM Member
            WHERE mobile = ?
        """, (mobilenumber,))
        mobile = self.cur.fetchone()
        con.commit()
        con.close()
        if mobile:
            return self.security.decrypt_data(mobile[0])
        return None
    
    def FetchMemberEmail(self, email):
        eMail = self.security.decrypt_data(email)
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            SELECT email FROM Member
            WHERE email = ?
        """, (eMail,))
        mail = self.cur.fetchone()
        con.commit()
        con.close()
        if mail:
            return self.security.decrypt_data(mail[0])
        return None
    
    def FetchConsUsername(self, consusername):
        name = self.encrypt_data(consusername)
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            SELECT username FROM Consultant
            WHERE username = ?
        """, (name,))
        username = self.cur.fetchone()
        con.commit()
        con.close()
        if username:
            return self.security.decrypt_data(username[0])
        return None
    
    def FetchConsultantID(self, user):
        username = self.encrypt_data(user.username)
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            SELECT id FROM Consultant
            WHERE username = ?
        """, (username,))
        id = self.cur.fetchone()[0]
        con.commit()
        con.close()
        return id
    
    def FetchSystemAdminID(self, user):
        username = self.encrypt_data(user.username)
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            SELECT id FROM SystemAdmin
            WHERE username = ?
        """, (username,))
        id = self.cur.fetchone()[0]
        con.commit()
        con.close()
        return id
    
    def FetchAdminUsername(self, adminusername):
        name = self.encrypt_data(adminusername)
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            SELECT username FROM SystemAdmin
            WHERE username = ?
        """, (name,))
        username = self.cur.fetchone()
        con.commit()
        con.close()
        if username:
            return self.security.decrypt_data(username[0])
        return None
import sqlite3
from Members import Member

class  DatabaseManager:
    '''This class handles database actions.'''
    dbname = "MealMemberManagement.db" 

    def __init__(self):
        
        self.con = sqlite3.connect(self.dbname)

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

        if username == "1" and password == "1":# superadmin - Admin_123?
            con.close()
            loggedInUser = SuperAdmin()
            return True, loggedInUser

        self.cur.execute("SELECT * FROM SystemAdmin WHERE username = ? AND password = ?", (username, password))
        user = self.cur.fetchone()

        if user:
            loggedInUser = SystemAdmin(user[1], user[2], user[3], user[4])
            loggedInUser.registrationdate = user[5]
            
            con.close()
            return True, loggedInUser

        self.cur.execute("SELECT * FROM Consultant WHERE username = ? AND password = ?", (username, password))
        user = self.cur.fetchone()

        con.close()

        if user:
            loggedInUser = Consultant(user[1], user[2], user[3], user[4])
            loggedInUser.registrationdate = user[5]
            return True, loggedInUser
        else:
            return False, None

################################################################################################
# CREATE here below   
    def createMember(self, member):
        '''Insert Data: Member.'''
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        self.cur.execute("""
            INSERT INTO Member (membershipID, firstname, lastname, registrationdate, age, gender, weight, adress, email, mobile)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (member.membershipID, member.firstname, member.lastname, member.registrationdate, member.age, member.gender, member.weight, member.adress, member.email, member.mobile))
        con.commit()
        con.close()

    def createConsultant(self,user):
        '''Insert Data: Consult.'''
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        self.cur.execute("""
            INSERT INTO Consultant (firstname, lastname, username, password, registrationdate)
            VALUES (?, ?, ?, ?, ?);
        """,
        
          (user.firstname, user.lastname, user.username, user.password, user.registrationdate))
        con.commit()
        con.close()

    def createSystemAdmin(self,user):
        '''Insert Data: System Admin.'''
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
        '''Update Data: Member.'''
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
        '''Update Data: Consultant.'''
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
        '''Update Data: System Admin.'''
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
        '''Reset password of System Admin.'''
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            UPDATE SystemAdmin
            SET password = ?
            WHERE username = ?;
        """, (newpassword, username))
        con.commit()
        con.close()

    def resetConsultantPassword(self, consultant):
        '''Reset password of Consultant.'''
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        self.cur.execute("""
            UPDATE Consultant
            SET password = ?
            WHERE username = ?;
        """, (consultant.password, consultant.username))
        con.commit()
        con.close()

    def resetSystemAdminPassword(self,sytemadmin):
        '''Reset password of System Admin.'''
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            UPDATE SystemAdmin
            SET password = ?
            WHERE username = ?;
        """, (sytemadmin.password, sytemadmin.username))
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

    def deleteConsultant(self,consultant):
        '''Delete Data: Consultant.'''
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        self.cur.execute("""
            DELETE FROM Consultant 
            WHERE username = ?;
        """, (consultant.username,))
        con.commit()
        con.close()

    def deleteSystemAdmin(self,systemadmin):
        '''Delete Data: System Admin.'''
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            DELETE FROM SystemAdmin 
            WHERE username = ?;
        """, (systemadmin.username,))
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
            systemAdmin = SystemAdmin(res[1], res[2], res[3], res[4])
            listUsers.append(systemAdmin)
        for res in listCons:
            consultant = Consultant(res[1], res[2], res[3], res[4])
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
            member = Member(mem[1], mem[2], mem[3], mem[4], mem[5], mem[6], mem[7], mem[8])
            member.membershipID = mem[0]
            listUsers.append(member)
        con.close()
        return listUsers

################################################################################################
# FETCHES here below
    def FetchMemberMobile(self, mobileNumber):
        '''Get specific Mobile data of Member from the database.'''
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            SELECT mobile FROM Member
            WHERE mobile = ?
        """, (mobileNumber,))
        mobile = self.cur.fetchone()
        con.commit()
        con.close()
        return mobile
    
    def FetchMemberEmail(self, email):
        '''Get specific Email data of Member from the database.'''
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            SELECT email FROM Member
            WHERE LOWER(email) = LOWER(?)
        """, (email,))
        mobile = self.cur.fetchone()
        con.commit()
        con.close()
        return mobile
    
    def FetchConsUsername(self, consusername):
        '''Get specific Username data of Consultant from the database.'''
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            SELECT username FROM Consultant
            WHERE LOWER(username) = LOWER(?)
        """, (consusername,))
        username = self.cur.fetchone()
        con.commit()
        con.close()
        return username
    
    def FetchConsultantID(self, user):
        '''Get specific ID data of Consultant from the database.'''
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            SELECT id FROM Consultant
            WHERE LOWER(username) = LOWER(?)
        """, (user.username,))
        id = self.cur.fetchone()[0]
        con.commit()
        con.close()
        return id
    
    def FetchSystemAdminID(self, user):
        '''Get specific ID data of SystemAdmin from the database.'''
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            SELECT id FROM SystemAdmin
            WHERE LOWER(username) = LOWER(?)
        """, (user.username,))
        id = self.cur.fetchone()[0]
        con.commit()
        con.close()
        return id
    
    def FetchAdminUsername(self, adminusername):
        '''Get specific Username data of System Admin from the database.'''
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            SELECT username FROM SystemAdmin
            WHERE LOWER(username) = LOWER(?)
        """, (adminusername,))
        username = self.cur.fetchone()
        con.commit()
        con.close()
        return username
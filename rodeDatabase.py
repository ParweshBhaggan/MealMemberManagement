import sqlite3

from Members import Member



class  DatabaseManager:
    dbname = "MealMemberManagement.db"
    

    def __init__(self):
        
        self.con = sqlite3.connect(self.dbname)

        self.cur = self.con.cursor()
        self.CreateMemberTable()
        self.CreateSystemAdminTable()
        self.CreateConsultantTable()
        self.con.commit()
        self.con.close()
    # self.cur.execute("DROP TABLE Member")
    # self.cur.execute("DROP TABLE Consultant")
    # self.cur.execute("DROP TABLE SystemAdmin")

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
            firstname TEXT NOT NULL,
            lastname TEXT NOT NULL,
            username TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            registrationdate DATE NOT NULL
        )
    """)

   

    def resetPassword(self,newpassword, username):
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            UPDATE SystemAdmin
            SET password = ?
            WHERE username = ?;
        """, (newpassword, username))
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

    def deleteSystemAdmin(self,systemadmin):
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            DELETE FROM SystemAdmin 
            WHERE username = ?;
        """, (systemadmin.username,))
        con.commit()
        con.close()
    # user word gevonden
    # pak zijn username
    # geef nieuwe values
    # geef params aan update()
    # user = SystemAdmin("newfirst", "newlast",gevondenuser.username, gevondnuser.password)
    # update(user)
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
    
    def FetchSystemAdminID(self, user):
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            SELECT id FROM SystemAdmin
            WHERE username = ?
        """, (user.username,))
        id = self.cur.fetchone()[0]
        con.commit()
        con.close()
        return id
    

    def resetSystemAdminPassword(self,sytemadmin):
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            UPDATE SystemAdmin
            SET password = ?
            WHERE username = ?;
        """, (sytemadmin.password, sytemadmin.username))
        con.commit()
        con.close()

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
            systemAdmin = SystemAdmin(res[1], res[2], res[3], res[4])
            listUsers.append(systemAdmin)
        for res in listCons:
            consultant = Consultant(res[1], res[2], res[3], res[4])
            listUsers.append(consultant)
        
        # for user in listUsers:
        #     print(user.firstname, user.lastname, user.username, user.password, user.registrationdate)
        con.close()
        return listUsers

    def createConsultant(self,user):
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        self.cur.execute("""
            INSERT INTO Consultant (firstname, lastname, username, password, registrationdate)
            VALUES (?, ?, ?, ?, ?);
        """, (user.firstname, user.lastname, user.username, user.password, user.registrationdate))
        con.commit()
        con.close()

    def deleteConsultant(self,consultant):
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        self.cur.execute("""
            DELETE FROM Consultant 
            WHERE username = ?;
        """, (consultant.username,))
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

    def FetchConsultantID(self, user):
        con = sqlite3.connect(self.dbname)
        self.cur= con.cursor()
        self.cur.execute("""
            SELECT id FROM Consultant
            WHERE username = ?
        """, (user.username,))
        id = self.cur.fetchone()[0]
        con.commit()
        con.close()
        return id

    def resetConsultantPassword(self, consultant):
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        self.cur.execute("""
            UPDATE Consultant
            SET password = ?
            WHERE username = ?;
        """, (consultant.password, consultant.username))
        con.commit()
        con.close()

    def createMember(self, member):
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        self.cur.execute("""
            INSERT INTO Member (membershipID, firstname, lastname, registrationdate, age, gender, weight, adress, email, mobile)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
        """, (member.membershipID, member.firstname, member.lastname, member.registrationdate, member.age, member.gender, member.weight, member.adress, member.email, member.mobile))
        con.commit()
        con.close()

    def deleteMember(self, member):
        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()
        self.cur.execute("""
            DELETE FROM Member 
            WHERE membershipID = ?;
        """, (member.membershipID,))
        con.commit()
        con.close()

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

    def getallMembers(self):
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
        # for member in listUsers:
            # print(member.membershipID, member.firstname, member.lastname, member.registrationdate, member.age, member.gender, member.weight, member.adress, member.email, member.mobile)
        con.close()
        return listUsers

    def loginUser(self, username, password):
        from User import Consultant, SuperAdmin, SystemAdmin

        con = sqlite3.connect(self.dbname)
        self.cur = con.cursor()

        if username == "super_admin" and password == "Admin_123?":
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

# db = DatabaseManager()
# admin = SystemAdmin("firstadmin", "lastadmin", "testadmin", "test")
# admin1 = SystemAdmin("firstadmin1", "lastadmin1", "testadmin1", "test")
# admin2 = SystemAdmin("firstadmin2", "lastadmin2", "testadmin2", "test")
# # createSystemAdmin(admin)
# # createSystemAdmin(admin1)
# # createSystemAdmin(admin2)

# consulant = Consultant("firstconsul", "lastconsul", "testconsul", "test")
# consulant1 = Consultant("firstconsul1", "lastconsul1", "testconsul1", "test")
# consulant2 = Consultant("firstconsul2", "lastconsul2", "testconsul2", "test")
# # createConsultant(consulant)
# # createConsultant(consulant1)
# # createConsultant(consulant2)

# member = Member('firstmember', 'lastmember', 30, 'M', 61.4, 'Streetname housenumber zipcode City', 'my@email.com', +31612345678)
# member1 = Member('firstmember1', 'lastmember1', 30, 'M', 61.4, 'Streetname housenumber zipcode City', 'my@email1.com', +31612345671)
# member2 = Member('firstmember2', 'lastmember2', 30, 'M', 61.4, 'Streetname housenumber zipcode City', 'my@email2.com', +31612345672)
# # createMember(member)
# # createMember(member1)
# # createMember(member2)

# db.getallSystemAdmins()
# getallConsultants()
# getallMembers()

# deleteSystemAdmin("testingadmin")
# deleteConsultant(consulant2.username)
# deleteMember()


# resetSystemAdminPassword("newpassword", "testadmin")
# resetConsultantPassword("newpassword", "testconsul")
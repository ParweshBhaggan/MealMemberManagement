import sqlite3

dbname = "MealMemberManagement.db"

con = sqlite3.connect(dbname)

cur = con.cursor()

# cur.execute("DROP TABLE Member")
# cur.execute("DROP TABLE Consultant")
# cur.execute("DROP TABLE SystemAdmin")

cur.execute("""
    CREATE TABLE IF NOT EXISTS Member(
        membershipID VARCHAR(255) PRIMARY KEY NOT NULL,
        firstname VARCHAR(255) NOT NULL,
        lastname VARCHAR(255) NOT NULL,
        registrationdate DATE NOT NULL,
        age INT NOT NULL,
        gender VARCHAR(50) NOT NULL,
        weight DECIMAL(5, 2) NOT NULL,
        adress TEXT NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE,
        mobile VARCHAR(20) NOT NULL UNIQUE
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS SystemAdmin(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        firstname VARCHAR(255) NOT NULL,
        lastname VARCHAR(255) NOT NULL,
        username VARCHAR(255) UNIQUE,
        password VARCHAR(255) NOT NULL,
        registrationdate DATE NOT NULL
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS Consultant (
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        firstname TEXT NOT NULL,
        lastname TEXT NOT NULL,
        username TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        registrationdate DATE NOT NULL
    )
""")

con.commit()
con.close()

def createSystemAdmin(user):
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    cur.execute("""
        INSERT INTO SystemAdmin (firstname, lastname, username, password, registrationdate)
        VALUES (?, ?, ?, ?, ?);
    """, (user.firstname, user.lastname, user.username, user.password, user.registrationdate))
    con.commit()
    con.close()

def getallSystemAdmins():
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    cur.execute("""
        SELECT * FROM SystemAdmin;
    """)
    print(cur.fetchall())
    con.close()

def deleteSystemAdmin(username):
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    cur.execute("""
        DELETE FROM SystemAdmin WHERE username = ?;
    """, (username,))
    con.commit()
    con.close()

def updateSystemAdmin(user):
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    cur.execute("""
        UPDATE SystemAdmin
        SET firstname = ?, lastname = ?
        WHERE username = ?;
    """, (user.firstname, user.lastname, user.username))
    con.commit()
    con.close()

def resetSystemAdminPassword(newpassword, username):
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    cur.execute("""
        UPDATE SystemAdmin
        SET password = ?
        WHERE username = ?;
    """, (newpassword, username))
    con.commit()
    con.close()

def createConsultant(user):
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    cur.execute("""
        INSERT INTO Consultant (firstname, lastname, username, password, registrationdate)
        VALUES (?, ?, ?, ?, ?);
    """, (user.firstname, user.lastname, user.username, user.password, user.registrationdate))
    con.commit()
    con.close()

def getallConsultants():
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    cur.execute("""
        SELECT * FROM Consultant;
    """)
    print(cur.fetchall())
    con.close()

def deleteConsultant(username):
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    cur.execute("""
        DELETE FROM Consultant 
        WHERE username = ?;
    """, (username,))
    con.commit()
    con.close()

def updateConsultant(user):
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    cur.execute("""
        UPDATE Consultant
        SET firstname = ?, lastname = ?
        WHERE username = ?;
    """, (user.firstname, user.lastname, user.username))
    con.commit()
    con.close()

def resetConsultantPassword(newpassword, username):
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    cur.execute("""
        UPDATE Consultant
        SET password = ?
        WHERE username = ?;
    """, (newpassword, username))
    con.commit()
    con.close()

def createMember(member):
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    cur.execute("""
        INSERT INTO Member (membershipID, firstname, lastname, registrationdate, age, gender, weight, adress, email, mobile)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?);
    """, (member.membershipID, member.firstname, member.lastname, member.registrationdate, member.age, member.gender, member.weight, member.adress, member.email, member.mobile))
    con.commit()
    con.close()

def deleteMember(memberid):
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    cur.execute("""
        DELETE FROM Member 
        WHERE membershipID = ?;
    """, (memberid,))
    con.commit()
    con.close()

def getallMembers():
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    cur.execute("""
        SELECT * FROM Member;
    """)
    print(cur.fetchall())
    con.close()

def updateMember(member):
    con = sqlite3.connect(dbname)
    cur = con.cursor()
    cur.execute("""
        UPDATE Consultant
        SET firstname = ?, lastname = ?, age = ?, gender = ?, weight = ?, adress = ?, email = ?, mobile = ?
        WHERE membershipID = ?;
    """, (member.firstname, member.lastname, member.username))
    con.commit()
    con.close()

def loginUser(username, password):
    con = sqlite3.connect(dbname)
    cur = con.cursor()

    if username == "super_admin" and password == "Admin_123?":
        con.close()
        return True, None, "SuperAdmin"

    cur.execute("SELECT * FROM SystemAdmin WHERE username = ? AND password = ?", (username, password))
    user = cur.fetchone()

    if user:
        con.close()
        return True, user, "SystemAdmin"

    cur.execute("SELECT * FROM Consultant WHERE username = ? AND password = ?", (username, password))
    user = cur.fetchone()

    con.close()

    if user:
        return True, user, "Consultant"
    else:
        return False, None, None


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

# getallSystemAdmins()
# getallConsultants()
# getallMembers()

# deleteSystemAdmin(admin1.username)
# deleteConsultant(consulant2.username)
# deleteMember()


# resetSystemAdminPassword("newpassword", "testadmin")
# resetConsultantPassword("newpassword", "testconsul")
    
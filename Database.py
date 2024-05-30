print("create connection SQLLite3")
import sqlite3

con = sqlite3.connect("MealMemberManagement.db")
print(con)

cur = con.cursor()

cur.execute("""
    CREATE TABLE IF NOT EXISTS Member(
        ID VARCHAR(255) PRIMARY KEY,
        firstname VARCHAR(255) NOT NULL,
        lastname VARCHAR(255) NOT NULL,
        registrationdate DATE NOT NULL,
        age INT NOT NULL,
        gender VARCHAR(50) NOT NULL,
        weight DECIMAL(5, 2) NOT NULL,
        adress TEXT NOT NULL,
        email VARCHAR(255) NOT NULL UNIQUE,
        mobile VARCHAR(20) NOT NULL UNIQUE,
        username VARCHAR(255) NOT NULL UNIQUE,
        password VARCHAR(255) NOT NULL
    )
""")

cur.execute("""
    CREATE TABLE IF NOT EXISTS SystemAdmin(
        firstname VARCHAR(255) NOT NULL,
        lastname VARCHAR(255) NOT NULL,
        username VARCHAR(255) UNIQUE,
        password VARCHAR(255) NOT NULL,
        registrationdate DATE NOT NULL
    )
""")

cur.execute("""
CREATE TABLE IF NOT EXISTS Consultant (
    firstname TEXT,
    lastname TEXT,
    username TEXT UNIQUE,
    password TEXT,
    registrationdate DATE
)
""")

con.commit()

res = cur.execute("SELECT name FROM sqlite_master")
print(res.fetchall())
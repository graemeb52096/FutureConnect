__author__ = 'BatesG1996'

# Houses classes for User data

#Before connecting to a MySQL database, make sure of the followings −

#You have created a database TESTDB.

#You have created a table EMPLOYEE in TESTDB.

#This table has fields FIRST_NAME, LAST_NAME, AGE, SEX and INCOME.

#User ID "testuser" and password "test123" are set to access TESTDB.

#Python module MySQLdb is installed properly on your machine.

import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Create University table
sql1 = """CREATE TABLE UNIVERSITY (
         EMAIL  CHAR(100) NOT NULL,
         PASSWORD  CHAR(100) NOT NULL,
         AGE CHAR(3) NOT NULL,
         FIRST_NAME CHAR(100) NOT NULL,
         LAST_NAME CHAR(100) NOT NULL,
         BIO CHAR(200),
         UNIVERSITY CHAR(100) NOT NULL,
         MAJOR CHAR(100))"""

# Create Highschool table
sql2 = """CREATE TABLE HIGHSCHOOLS (
         EMAIL CHAR(100) NOT NULL,
         PASSWORD CHAR (100) NOT NULL,
         AGE CHAR(3) NOT NULL,
         FIRST_NAME CHAR(100) NOT NULL,
         LAST_NAME CHAR(100) NOT NULL,
         BIO CHAR(200),
         HIGHSCHOOL CHAR(100) NOT NULL,)"""

cursor.execute(sql1)
cursor.execute(sql2)

# disconnect from server
db.close()






class User:

    def __init__(self, email, password, first, last, bio, age):

        self.email, self.password, self.first, self.last, self.bio = \
        email, password, first, last, bio, age

    def delete_user(self, user):
        pass
        #delete user

    def get_data(self):
        pass
        #return database data


class HighSchool(User):

    def __init__(self, email, password, first, last, bio, age, high_school):

        super(HighSchool, self).__init__(email, password, first, last, bio, age)
        self.high_school = high_school

        #the SQL commands
        sql = """INSERT INTO UNIVERSITY (
                        EMAIL, PASSWORD, AGE, FIRST_NAME, LAST_NAME, BIO,
                        HIGHSCHOOL)
                        VALUES ({0},{1},{2},{3},{4},{5},{6})"""
        cursor.execute(sql.format(self.email, self.password, self.age,
                                  self.first, self.last,self.bio,
                                  self.high_school))

class University(User):

    def __init__(self, email, password, first, last, bio, age, university,
                 major):

        super(University, self).__init__(email, password, first, last, bio, age)
        self.university, self.major = university, major

    def add_uni(self):
        #the SQL commands
        sql = """INSERT INTO UNIVERSITY (
                        EMAIL, PASSWORD, AGE, FIRST_NAME, LAST_NAME, BIO,
                        UNIVERSITY, MAJOR)
                        VALUES ({0},{1},{2},{3},{4},{5},{6},{7})"""
        cursor.execute(sql.format(self.email, self.password, self.age,
                                  self.first, self.last,self.bio,
                                  self.university, self.major))






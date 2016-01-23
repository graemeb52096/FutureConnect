__author__ = 'BatesG1996'

# Houses classes for User data

#Before connecting to a MySQL database, make sure of the followings −

#You have created a database TESTDB.

#You have created a table EMPLOYEE in TESTDB.

#This table has fields FIRST_NAME, LAST_NAME, AGE, SEX and INCOME.

#User ID "testuser" and password "test123" are set to access TESTDB.

#Python module MySQLdb is installed properly on your machine.
'''
import MySQLdb

# Open database connection
db = MySQLdb.connect("localhost","testuser","test123","TESTDB" )

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Create User table with information ALL Users have
sql1 = """CREATE TABLE USERS (
         EMAIL  CHAR(100) NOT NULL,
         PASSWORD  CHAR(100),
         AGE INT,
         FIRST_NAME CHAR(100),
         LAST_NAME CHAR(100))"""

# Create Highschool table
sql2 = """CREATE TABLE HIGHSCHOOLS (
         HIGHSCHOOL  CHAR(100) NOT NULL)"""

cursor.execute(sql)

# Fetch a single row using fetchone() method.
data = cursor.fetchone()

print "Database version : %s " % data

# disconnect from server
db.close()




'''

class User:

    def __init__(self, email, password, first, last, bio):

        self.email, self.password, self.first, self.last, self.bio = \
        email, password, first, last, bio

    def add_user(self, user):
        pass
        #add user to database

    def delete_user(self, user):
        pass
        #delete user

    def get_data(self):
        pass
        #return database data



class Highschool(User):

    def __init__(self, email, password, first, last, bio, highschool):

        super(Highschool, self).__init__(email, password, first, last)
        self.highschool = highschool


class University(User):

    def __init__(self, email, password, first, last, bio, university, major):

        super(University, self).__init__(email, password, first, last)
        self.university, self.major = university, major







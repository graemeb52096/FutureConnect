__author__ = 'BatesG1996'

# Houses classes for User data
'''
import MySQLdb

#creates database

db1 = MS.connect(host="localhost",user="root",passwd="****")
cursor = db1.cursor()
sql = 'CREATE DATABASE mydata'
cursor.execute(sql)


#creates table

sql = CREATE TABLE foo (
       bar VARCHAR(50) DEFAULT NULL
       ) ENGINE=MyISAM DEFAULT CHARSET=latin1

cursor.execute(sql)




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







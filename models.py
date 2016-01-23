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

    def __init__(self, email, password, first, last):

        self.email, self.password, self.first, self.last = \
        email, password, first, last

    def add_user(self, user):

        #add user to database
        pass

    def delete_user(self, user):
        pass
        #delete user

    def get_data(self):

        #return database data
        pass



class Highschool(User):

    def __init__(self, email, password, first, last, highschool):

        super(Highschool, self).__init__(email, password, first, last)
        self.highschool = highschool


class University(User):

    def __init__(self, email, password, first, last, university, major):

        super(University, self).__init__(email, password, first, last)
        self.university, self.major = university, major







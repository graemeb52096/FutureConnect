import MySQLdb

db = MySQLdb.connect("localhost", "root", "265358", "usersdb")

cursor = db.cursor()

db.close()


class User:
    def add_user(self):
        '''

        Adds user to table.
        Consists of SQL

        :return:
        '''
        # If role is admin add to Users table
        if self.role == 0:
            pass
        # Else if role is High School add to users
        # and high school table
        elif self.role == 1:
            pass
        # Else(role is P.S.) add to users table
        # and Post Secondary table
        else:
            pass

    def remove_user(self):
        '''

        Removes user from table.
        Consists of SQL

        :return:
        '''
        # If role is admin remove from Users table
        if self.role == 0:
            pass
        # Else if role is High School remove from users
        # and high school table
        elif self.role == 1:
            pass
        # Else(role is P.S.) remove from users table
        # and Post Secondary table
        else:
            pass

    def __init__(self, email, password, role, first, last, bio):
        '''
        :param email: users email
        :param password: users password
        :param role: Users Role Admin(0), HighSchool(1), PostSecondary(2)
        :param first: Users First Name
        :param last: Users Last Name
        :param bio: Quick Bio for user
        :return: None
        '''

        self.email = email
        self.password = password
        self.role = role
        self.first = first
        self.last = last
        self.bio = bio


class HighSchool(User):
    def __init__(self, email, password, first, last, bio, year, high_school):
        super(HighSchool, self).__init__(email, password, first, last, bio, year)
        self.high_school = high_school
        self.year = year

class Mentor(User):
    def __init__(self, email, password, first, last, bio, university,
                 major, year):
        super(Mentor, self).__init__(email, password, first, bio)
        self.university = university
        self.major = major
        self.year = year

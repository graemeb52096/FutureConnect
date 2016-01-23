import MySQLdb

db = MySQLdb.connect("localhost", "root", "data", "FutureConnectDev")
cursor = db.cursor()


class User:
    def add_user(self):
        '''

        Adds user to table.
        Consists of SQL

        :return: User instance
        '''
        insert_user_sql = (
            "INSERT INTO Users "
            "(fName, lName, email, bio, role, password) "
            "VALUES "
            "('%s', '%s', '%s', '%s', '%s', '%s')"% (
                self.first,
                self.last,
                self.email,
                self.bio,
                self.role,
                self.password
            )
        )
        # Insert User into DB
        cursor.execute(insert_user_sql)
        db.commit()


    def remove_user(self):
        '''

        Removes user from table.
        Consists of SQL

        :return:
        '''
        pass

    def __init__(self, email, password, first, last, bio):
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
        self.role = 0
        self.first = first
        self.last = last
        self.bio = bio


class HighSchool(User):

    def add_HighSchooler(self):
        pass

    def __init__(
            self, email, password, first, last, bio, high_school
        ):

        super(HighSchool, self).__init__(email, password, first, last, bio)
        self.school = high_school
        self.role = 1

class Mentor(User):

    def add_Mentor(self):
        pass
    
    def __init__(
            self, email, password, first,
            last, bio, university, major, year
        ):
        super(Mentor, self).__init__( email, password, first, last, bio)
        self.university = university
        self.major = major
        self.year = year
        self.role = 2
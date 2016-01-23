
import MySQLdb

db = MySQLdb.connect("localhost","root","265358","usersdb" )

cursor = db.cursor()

db.close()

class User:

    def __init__(self, email, password, type, first, last, bio):

        self.email = email
        self.password = password
        self.type = type
        self.first = first
        self.last = last
        self.bio = bio

        sql = "INSERT INTO Users (email, password," \
              "user_type, bio, first_name, last_name)" \
              "VALUES ({0}, {1}, {2}, {3}, {4}, {5});"

        cursor.execute(sql.format(self.email, self.password,
                                  self.type, self.bio,
                                  self.first, self.last))
    def edit_info(self):

        raise NotImplementedError('Implemented in a subclass')


class HighSchool(User):

    def __init__(self, email, password, first, last, bio, year, high_school):

        super(HighSchool, self).__init__(email, password, first, last, bio, year)

        self.high_school = high_school
        self.year = year

        #the SQL commands

        q = "INSERT INTO GoesToHS (email, school, grade)" \
            "SELECT email, {0} as school, major, {1} as grade" \
            "FROM User" \
            "WHERE User.email = {2};"

        cursor.execute(q.format(self.high_school, self.year, self.email))

    def edit_info(self, pw, yr, fn, ln, bio, ut):

        q = "UPDATE GoesToHS" \
            "SET user_type = {7}, bio = {5}," \
            "first_name = {3}, last_name = {4}," \
            "school = {6}, year = {2}, password = {1}" \
            "WHERE email = {0};"

        cursor.execute(q.format(self.email, pw, yr, fn, ln, bio, ut))


class Mentor(User):

    def __init__(self, email, password, first, last, bio, university,
                 major, year):

        super(Mentor, self).__init__(email, password, first, bio)

        self.university = university
        self.major = major
        self.year = year

        q = "INSERT INTO GoesToUni (email, school, major, year)" \
              "SELECT email, university as school, major, {0} as year" \
              "FROM User, Universities, Major" \
              "WHERE User.email = {1}" \
              "AND Universities.uni = {2}" \
              "AND Majors.major = {3};"

        cursor.execute(q.format(self.year, self.email, self.university, self.major))

    def edit_info(self, pw, yr, fn, ln, bio, uni, major, type):

        q = "UPDATE GoesToUni" \
            "SET school = (SELECT uni" \
                            "FROM Universities" \
                            "WHERE uni = {6}), " \
                "major = (SELECT major" \
                            "FROM Majors" \
                            "WHERE major = {7})," \
            "user_type = {8}, bio = {5}," \
            "first_name = {3}, last_name = {4}," \
            "year = {2}, password = {1}" \
            "WHERE email = {0};"

        cursor.execute(q.format(self.email, pw, yr, fn, ln, bio, uni, major, type))

    def


class Admin(User):

    def __init__(self, email, password, first, last, bio, age):
        super(Admin, self).__init__(email, password, first, last, bio, age)
        #Admin does not take any special arguments

    def delete_user(self, email):

        q = "DELETE FROM GoesToHS" \
            "WHERE email = {0};" \
            "DELETE FROM GoesToUni" \
            "WHERE email = {0};" \
            "DELETE FROM Users" \
            "WHERE email = {0};"

        cursor.execute(q.format(email))





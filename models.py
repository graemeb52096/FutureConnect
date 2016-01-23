__author__ = 'BatesG1996'

# Houses classes for User data

class User:

    def __init__(self, email, password, first, last):

        self.email, self.password, self.first, self.last = \
        email, password, first, last

class Highschool(User):

    def __init__(self, email, password, first, last, highschool):

        super(Highschool, self).__init__(email, password, first, last)
        self.highschool = highschool


class University(User):

    def __init__(self, email, password, first, last, university, major):

        super(University, self).__init__(email, password, first, last)
        self.university, self.major = university, major







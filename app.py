__author__ = 'BatesG1996'

from flask import Flask
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

def Authenticate(cred):
    '''

    User authentication.

    :param cred: Credentials Dictionary(email, password)
     :type cred: Dict{}
    :return: Returns True/False response with message.
     :rtype: Dict{}
    '''
    # Validate User
    try:
        # Check users for given email
        goal_User = Users[cred['email']]
    # If user is not found, return key error
    except KeyError:
        return {
            'Response': 'False',
            'Message': 'Invalid email'
        }
    # Once User is Validated, check if password is a match
    if goal_User['password'] == cred['password']:
        # If match, return True
        return {
            'Response': 'True',
            'Message': 'Credentials Correct'
        }
    else:
        # Else, return False
        return {
            'Response': 'False',
            'Message': 'Password incorrect'
        }

class Login:

    def get(self):
        pass

'''
==== Begin Test Cases ===
'''
Graeme = {
    'fName': 'Graeme',
    'lName': 'Bates',
    'email': 'batesg1996@gmail.com',
    'password': 'password'
}

Test = {
    'fname': 'User',
    'lName': 'Null',
    'email': 'test@example.com',
    'password': 'password'
}

Users = {'batesg1996@gmail.com': Graeme, 'test@example.com': Test}
class TestUserResponse(Resource):
    def get(self):
        return {
            'Users': Users
        }
api.add_resource(TestUserResponse, '/Users')
'''
==== End Test Cases ===
'''

if __name__ == "__main__":
    app.run(debug=True)
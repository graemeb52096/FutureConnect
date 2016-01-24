__author__ = 'BatesG1996'

from flask import Flask, request, make_response, current_app
from flask_restful import Resource, Api
from flask_cors import CORS
import json
import models

app = Flask(__name__)
api = Api(app)
CORS(app)

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
        response = {
            'Response': 'False',
            'Message': 'Invalid email'
        }
        return response
    # Once User is Validated, check if password is a match
    if goal_User['password'] == cred['password']:
        # If match, return True
        response = {
            'Response': 'True',
            'Message': 'Credentials Correct',
            'Data': goal_User['email']
        }
        return response
    else:
        # Else, return False
        response = {
            'Response': 'False',
            'Message': 'Password incorrect'
        }
        return response

@app.route('/login', methods=['POST'])
def login():
    if request.method == 'POST':
        data = json.loads(request.data)
        response = Authenticate(data)
        return json.dumps(response)
    else:
        pass

@app.route('/register', methods=['POST'])
def register():

    if request.method == 'POST':
        data = json.loads(request.data)
        print data['role']
        if int(data['role']) == 2:
            new_mentor = models.Mentor(
                data['email'],
                data['password'],
                data['first'],
                data['last'],
                data['bio'],
                data['school'],
                data['major']
            )

            new_mentor.add_Mentor()
            return json.dumps({'Response': 'Added new Mentor'})

        elif int(data['role']) == 1:
            new_highschool = models.HighSchool(
                data['email'],
                data['password'],
                data['first'],
                data['last'],
                data['bio'],
                data['school']
            )

            new_highschool.add_HighSchooler()
            return json.dumps({'Response': 'Added new HighSchool Student'})
    else:
        return json.dumps({'Response': 'False'})

@app.route('/users', methods=['GET'])
def users():

    Users, Mentors = models.get_user_information()

    pass

'''
==== Begin Test Cases ===
'''
Graeme = {
    'fName': 'Graeme',
    'lName': 'Bates',
    'email': 'batesg1996@gmail.com',
    'password': 'password',
    'type': 2,
    'program': 'Computer Science',
    'uni': 'University of Toronto'

}
Joe = {
    'fName': 'Joe',
    'lName': 'Smith',
    'email': 'joesmith@gmail.com',
    'password': 'password',
    'type': 2,
    'program': 'Philosophy',
    'uni': 'University of British Columbia'

}

Test = {
    'fName': 'User',
    'lName': 'Null',
    'email': 'test@example.com',
    'password': 'password'
}

Users = {
    'batesg1996@gmail.com': Graeme,
    'test@example.com': Test,
    'joesmith@gmail.com': Joe
}
class TestUserResponse(Resource):
    def get(self):
        return {
            'Users': Users
        }
class TestServer(Resource):
    def get(self):
        return '<h1>Test</h1>'

api.add_resource(TestUserResponse, '/Users')
api.add_resource(TestServer, '/')
'''
==== End Test Cases ===
'''

#if __name__ == "__main__":
#    app.run(debug=True)

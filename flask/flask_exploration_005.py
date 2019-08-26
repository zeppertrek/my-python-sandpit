# flask_exploration_005.py  
# set FLASK_APP=flask_exploration_005.py
# set FLASK_DEBUG=1
# python -m flask run

# User session management in Flask using the flask_login extension 
# 
from flask import Flask, session, redirect, url_for, escape, request
#from flask_login import login_manager
from flask_login import LoginManager, login_required, login_user, logout_user 
# Custom User class defined in models 

# Simulating a DB.  Storing users in a dictionary 
#import db.user_db.user_db_list  as user_db_list
from db.user_db import user_db_list   
# import models.User  as User
from models.User import User


app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Integrating the login manager with the Flask "app" 
login_manager = LoginManager()
login_manager.init_app(app)


###################################################################
#
# What does this do ? 
@login_manager.user_loader
def user_loader(email):
    if email not in user_db_list.keys():
        return None 

    user = User()
    user.id = email
    return user


# What does this do ? 
@login_manager.request_loader
def request_loader(request):
    email = request.form.get('email')
    if email not in user_db_list.keys():
        return

    user = User()
    user.id = email

    # DO NOT ever store passwords in plaintext and always compare password
    # hashes using constant-time comparison!
    user.is_authenticated = request.form['password'] == user_db_list[email]['password']

    return user


###########################
# Create your own User Class 
# implement these properties and methods:
# is_authenticated, is_active, is_anonymous, 
# get_id() - This method must return a unicode that uniquely identifies this user
#@login_manager.user_loader
#def load_user(user_id):
#    return User.get_id(user_id)
	

# Views that require your users to be logged in can be decorated with the login_required decorator
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return 'Logged out'
	
# Views that require your users to be logged in can be decorated with the login_required decorator
@app.route("/settings")
@login_required
def settings():
    pass
	
# provide a callback for login failures:
@login_manager.unauthorized_handler
def unauthorized_handler():
    return 'Unauthorized'
	

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return '''
               <form action='login' method='POST'>
                <input type='text' name='email' id='email' placeholder='email'/>
                <input type='password' name='password' id='password' placeholder='password'/>
                <input type='submit' name='submit'/>
               </form>
               '''

    email = request.form['email']
    if request.form['password'] == user_db_list[email]['password']:
        user = User()
        user.id = email
        login_user(user)
        return redirect(url_for('protected'))

    return 'Bad login'
	
@app.route('/protected')
@login_required
def protected():
    return 'Logged in as: ' + flask_login.current_user.id
	

if __name__ == '__main__':
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.run(debug=False)
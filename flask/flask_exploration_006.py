# flask_exploration_006.py  
# set FLASK_APP=flask_exploration_006.py
# set FLASK_DEBUG=1
# python -m flask run

# User session management in Flask using the flask_login extension 
# 
from flask import Flask, session, redirect, url_for, escape, request
#from flask_login import various modules 
from flask_login import LoginManager, login_required, login_user, logout_user, current_user 
# Simulating a DB.  Storing users in a dictionary 
#import db.user_db.user_db_list  as user_db_list
from db.user_db import user_db_list   
# Custom User class defined in models 
# import models.User  as User
from models.SteroidUser import SteroidUser


app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Integrating the login manager with the Flask "app" 
login_manager = LoginManager()
login_manager.init_app(app)

# 
# Customizing the Login Process 
login_manager.login_view = "/login"
login_manager.login_message = "You gotta login"
login_manager.login_message_category = "info"



#  provide a user_loader callback. This callback is used to reload the user object from the user ID stored in the session. 
#  It should take the unicode ID of a user, and return the corresponding user object.
# 
@login_manager.user_loader
def user_loader(email):
    if email not in user_db_list.keys():
        return None 

    user = SteroidUser()
    user.id = email
    user.email = email 
    return user


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
        user = SteroidUser()
        user.email = email 
        user.id = email
        # Understand significance of remember=True 
        #login_user(user, remember=True)
        # login_user(user, remember=False, duration=None, force=False, fresh=True)
        bLogFlag = login_user(user, remember=True, force=True)
        print ( "User's Email ID is : " + user.get_id())
        if bLogFlag:
            print ( "login_user(user) returned TRUE")
        else:
            print ( "login_user(user) returned FALSE")
        return redirect(url_for('login_success'))

    return 'Bad login'

# Views that require your users to be logged in can be decorated with the login_required decorator
@app.route("/user_info")
@login_required
def user_info():
    # After logging in, how do I retrieve the credentials of the logged in user 
    mstr = "Current User status - "    
    if current_user.is_authenticated:
        mstr = mstr + "authenticated"	
    return  "User Info" + mstr 


# Views that require your users to be logged in can be decorated with the login_required decorator
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return 'Logged out'
	
@app.route('/login_success')
def login_success():
    return 'Managed to login successfully'

if __name__ == '__main__':
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.run(debug=False)

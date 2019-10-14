# flask_exploration_007.py  
# set FLASK_APP=flask_exploration_007.py
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

####################################################################################
####################################################################################

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
        return redirect(url_for('login_success'))

    return 'Bad login'


# Sometimes you want to login users without using cookies, such as using header values or an api key passed as a query argument. 
# In these cases, you should use the request_loader callback. 
# This callback should behave the same as your user_loader callback, except that it accepts the Flask request instead of a user_id.
# For example, to support login from both a url argument and from Basic Auth using the Authorization header:

@login_manager.request_loader
def load_user_from_request(request):

    # first, try to login using the api_key url arg
    api_key = request.args.get('api_key')
    if api_key:
        user = User.query.filter_by(api_key=api_key).first()
        if user:
            return user

    # next, try to login using Basic Auth
    api_key = request.headers.get('Authorization')
    if api_key:
        api_key = api_key.replace('Basic ', '', 1)
        try:
            api_key = base64.b64decode(api_key)
        except TypeError:
            pass
        user = User.query.filter_by(api_key=api_key).first()
        if user:
            return user

    # finally, return None if both methods did not login the user
    return None
	

if __name__ == '__main__':
    app.config['PROPAGATE_EXCEPTIONS'] = True
    app.run(debug=False)


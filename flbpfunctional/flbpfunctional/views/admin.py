# admin.py for flbpfunctional 

from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_login import login_user, current_user, login_required, logout_user

from flbpfunctional.models import SteroidUser
# 
#from flblueprints import db
from flbpfunctional.db.user_db import user_db_list 



# template_folder='templates_dir', static_folder='static_dir')
# In this case, Flask will look for templates and static assets in the templates_dir and static_dir directories inside the blueprint package.
# The template path added by a blueprint has lower priority than the application’s templates directory. 

#  
users_blueprint = Blueprint('admin', __name__, template_folder="D:/workspaces/my-python-sandpit/flbpfunctional/flbpfunctional/templates/admin")


################
#### routes ####
################

@users_blueprint.route('/profile')
@login_required
def profile():
    return render_template('profile.html')


@users_blueprint.route('/login', methods=['GET', 'POST'])
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
        #return redirect(url_for('login_success'))
        flash('Thanks for logging in, {}!'.format(current_user.email))
        return redirect(url_for('admin.profile'))
    return 'Bad login'

@users_blueprint.route('/logout')
@login_required
def logout():
    user = current_user
    user.authenticated = False
    logout_user()
    flash('Goodbye!')
    return redirect(url_for('admin.login'))
    #return 'Logged Out' 




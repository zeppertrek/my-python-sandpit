# [SANJIV NAGRAJ]
#/flblueprints/users/routes.py

#################
#### imports ####
#################

from flask import render_template, request, flash, redirect, url_for
from flask_login import login_user, current_user, login_required, logout_user

from . import users_blueprint
#from .forms import RegisterForm, LoginForm
from flblueprints.models import SteroidUser
# 
#from flblueprints import db
from db.user_db import user_db_list 


################
#### routes ####
################

@users_blueprint.route('/profile')
@login_required
def profile():
    return render_template('users/profile.html')


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
        return redirect(url_for('users.profile'))
    return 'Bad login'

@users_blueprint.route('/logout')
@login_required
def logout():
    user = current_user
    user.authenticated = False
    #db.session.add(user)
    #db.session.commit()
    logout_user()
    flash('Goodbye!')
    return redirect(url_for('recipes.index'))
    #return 'Logged Out' 




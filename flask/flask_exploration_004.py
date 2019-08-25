# flask_exploration_004.py  
# set FLASK_APP=flask_exploration_004.py
# set FLASK_DEBUG=1
# python -m flask run

# Cookie / Session Management in Flask 
# First steps towards building authentication into backend APIs 

# Another option is to use JWTs 

# Flask by default uses something called ‘signed cookies’. 
# This is simply a way of # storing the current session data on the client (rather than the server).
# In theory, it is meant to be done in such a way that it cannot be tampered with

# One of the drawbacks of this approach, however, is that the cookies are not encrypted, they’re signed. 
# This means that the content of the session can be read without the secret key

# Import all the flask relevant dependencies 
from flask import Flask, session, redirect, url_for, escape, request

app = Flask(__name__)

# Set the secret key to some random bytes. Keep this really secret!
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in'

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # Additional method for storing the password 
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))
	
	
def showdetails
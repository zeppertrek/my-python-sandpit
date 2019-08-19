# flask_exploration_001.py  
# set FLASK_APP=flask_exploration_001.py
# set FLASK_DEBUG=1
# python -m flask run
#
# Basic Flask program to demonstrate the use of routes to process requests 
#
# Routing is one of the most important concepts in Web / REST API development
# 
#

from flask import Flask, request, url_for, redirect 

# Creating an instance of the Flask class
app = Flask(__name__)

print ("Value of __name__ is %s", __name__)

# This is the decorator defined in the Flask class. Refer to class decorators  
@app.route('/')
def hello_world():
    return 'Hello, World!'
	
@app.route('/wrltfe')
def hello():
    return 'Would RLTFE'
	
@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username
	

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/path/<path:subpath>')
def show_subpath(subpath):
    # show the subpath after /path/
    return 'Subpath %s' % subpath
	
	

# Note - Slash at the end 
@app.route('/projects/')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'
	
	
@app.route('/getorpost', methods=['GET', 'POST'])
def getorpost():
    if request.method == 'POST':
        
        return 'POST POST REMEMBER THE POST MAN' + request.method  
    else:
        return 'GET GET GET ME A RETIREMENT PLAN' + request.method  


@app.route('/rd')
def rd():
    return redirect(url_for('ninja'))
	
@app.route('/ninja')
def ninja():
    return 'Index Page Ninja'


# What does this DO ? 
with app.test_request_context():
    # print(url_for('index'))
    print(url_for('login'))
    print(url_for('login', next='/'))
    print(url_for('profile', username='John Doe'))
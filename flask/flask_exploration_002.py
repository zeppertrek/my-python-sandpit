# flask_exploration_002.py  
# set FLASK_APP=flask_exploration_002.py
# set FLASK_DEBUG=1
# python -m flask run
#
# This will run a development server that is NOT meant to be used for production purposes 
# 
# Basic Flask program to demonstrate the use of routes to process requests 
#
# Routing is one of the most important concepts in Web / REST API development
# 
#

from flask import Flask, redirect, url_for
app = Flask(__name__)

# What if I define app2 = Flask() or app2 = Flask ("imthedim") ? 

@app.route('/admin')
def hello_admin():
   return 'Hello Admin'

@app.route('/guest/<guest>')
def hello_guest(guest):
   return 'Hello %s as Guest' % guest


# Demonstrating the use of url_for and redirect 
@app.route('/user/<name>')
def hello_user(name):
   if name =='admin':
      return redirect(url_for('hello_admin'))
   else:
      return redirect(url_for('hello_guest',guest = name))

if __name__ == '__main__':
   app.run(debug = True)
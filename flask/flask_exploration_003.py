# flask_exploration_003.py  
# set FLASK_APP=flask_exploration_003.py
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

from flask import Flask, redirect, url_for, jsonify, request, render_template 
app = Flask(__name__)

###################app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


# What if I define app2 = Flask() or app2 = Flask ("imthedim") ? 

def valid_names ( fn, ln):
    return True

# This route will display a page that has a HTML form which will POST data to the server
@app.route ('/displayform')
def displayform():
    return render_template ('userform.html')

def display_request_details(req):
    print (req.method)
    print (req.cookies)

# This will handle the POST request 
@app.route('/postform', methods=['POST', 'GET'])
def login():
    error = None
    if request.method == 'POST':
        if valid_names(request.form['firstname'], request.form['lastname']):
            display_request_details(request)
            return jsonify ( request.form['firstname'], request.form['lastname'] )
        else:
            error = 'Invalid username/password'
    # the code below is executed if the request method
    # was GET or the credentials were invalid
    return render_template('error.html', error=error)




if __name__ == '__main__':
   app.run(debug = True)
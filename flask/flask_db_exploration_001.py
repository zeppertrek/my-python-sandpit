# flask_db_exploration_001.py  
# set FLASK_APP=flask_db_exploration_001.py
# set FLASK_DEBUG=1
# python -m flask run
# 
# Using httpie as a tool to test the request 
# http POST http://127.0.0.1:5000/mprequest id=1000 target=1002
# http GET http://127.0.0.1:5000/mprequest
# 
# This will run a development server that is NOT meant to be used for production purposes 
# 
# Very basic SQLAlchemy example 
#

from flask import Flask, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
#

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://postgres@localhost:5432/dockerdb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

# just for a lark, db changed to dbxx 
dbxx = SQLAlchemy(app)

class Mp(dbxx.Model):
    id     = dbxx.Column(db.Integer, primary_key=True)
    target = dbxx.Column(db.Integer, unique=False, nullable=True)

    def __repr__(self):
        return '<id {}>'.format(self.id)
		
		

@app.route('/mprequest', methods=['POST', 'GET'])
def handle_mp():
    if request.method == 'POST':
        if request.is_json:
            data = request.get_json()
            new_mp = Mp(id=data['id'], target=data['target'])
            dbxx.session.add(new_mp)
            dbxx.session.commit()
            return {"message": f"mp {new_mp.id} has been created successfully."}
        else:
            return {"error": "The request payload is not in JSON format"}

    elif request.method == 'GET':
        mplist = Mp.query.all()
        results = [
            {
                "id": mpx.id,
                "target": mpx.target
            } for mpx in mplist]

        return {"count": len(results), "mp": results}
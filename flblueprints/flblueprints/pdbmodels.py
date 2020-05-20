# pdbmodels.py 
# 
# from sqlalchemy.dialects.postgresql import JSON  -- For JSON data types 
# db.Column(JSON), db.String() 

from app import pdbx
class Mp(pdbx.Model):
    id     = pdbx.Column(pdbx.Integer, primary_key=True)
    target = pdbx.Column(pdbx.Integer, unique=False, nullable=True)

    def __repr__(self):
        return '<id {}>'.format(self.id)
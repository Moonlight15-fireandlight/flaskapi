#from flask_sqlalchemy import SQLAlchemy
from source import db

#class Register(db.Model):
#    id = db.Column(db.Integer(), primary_key=True)
#    name = db.Column(db.String(length=30), nullable=False, unique = True)
#    #area = db.Column(db.String(length=20), nullable=False, unique = True)
#    correo = db.Column(db.String(length=50), nullable=False, unique = True)
#    #especialidad = db.Column(db.String(length=20), nullable=False, unique = True)
#    #ticket = db.Column(db.Integer(), nullable=False)
#    
#    def __repr__(self):
#        return f'Item {self.name}'

#db = SQLAlchemy()

class data_register(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(length=40), nullable=False, unique = True)
    especialidad = db.Column(db.String(length=30), nullable=False)
    correo = db.Column(db.String(length=50), nullable=False, unique = True)

    def __repr__(self):
        return f'Item {self.name}'
    


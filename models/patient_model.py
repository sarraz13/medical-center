from .db import db

class Patient(db.Model):
    __tablename__ = 'patient'  
    id = db.Column(db.Integer, primary_key=True)
    nom = db.Column(db.String(50), nullable=False)
    prenom = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    telephone = db.Column(db.String(20), nullable=False)



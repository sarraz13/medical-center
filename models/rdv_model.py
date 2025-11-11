from models.db import db
from models.patient_model import Patient  

class RDV(db.Model):
    __tablename__ = 'rdv'
    id = db.Column(db.Integer, primary_key=True)
    patient_id = db.Column(db.Integer, db.ForeignKey('patient.id'), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    raison = db.Column(db.String(255), nullable=False)
    statut = db.Column(db.String(20), nullable=False)

    patient = db.relationship('Patient', backref='rdvs')


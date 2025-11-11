from flask import Blueprint, render_template, request, redirect, url_for, flash
from models.rdv_model import RDV
from models.patient_model import Patient
from models.db import db
from datetime import datetime

# Définir un blueprint pour les routes des rendez-vous
rdv_bp = Blueprint('rdvs', __name__)

@rdv_bp.route('/ajouter', methods=['GET', 'POST'])
def ajouter_rdv():
    if request.method == 'POST':
        # 1. Créer le patient
        patient = Patient(
            nom=request.form['patient_nom'],
            prenom=request.form['patient_prenom'],
            email=request.form['patient_email'],
            telephone=request.form['patient_telephone']
        )
        db.session.add(patient)
        db.session.commit()

        # 2. Créer le RDV
        date = request.form['date']
        heure = request.form['heure']
        raison = request.form['raison']
        
        # Combine date et heure pour avoir un datetime si besoin
        datetime_rdv = f"{date} {heure}"

        rdv = RDV(
            patient_id=patient.id,
            date=datetime_rdv,
            raison=raison,
            statut="pending"  # Statut automatiquement à "En attente"
        )
        db.session.add(rdv)
        db.session.commit()

        # 3. Message flash de confirmation
        flash("✅ Rendez-vous ajouté avec succès !")
        return redirect(url_for('rdvs.liste_rdv'))

    return render_template('rdv_form.html')

@rdv_bp.route('/liste')
def liste_rdv():
    rdvs = RDV.query.all()
    return render_template('rdv_list.html', rdvs=rdvs)

@rdv_bp.route('/confirmer/<int:rdv_id>', methods=['POST'])
def confirmer_rdv(rdv_id):
    rdv = RDV.query.get_or_404(rdv_id)
    if rdv.statut == 'pending':
        rdv.statut = 'confirmed'
        db.session.commit()
    return redirect(url_for('rdvs.liste_rdv'))

@rdv_bp.route('/annuler/<int:rdv_id>', methods=['POST'])
def annuler_rdv(rdv_id):
    rdv = RDV.query.get_or_404(rdv_id)
    if rdv.statut != 'canceled':
        rdv.statut = 'canceled'
        db.session.commit()
    return redirect(url_for('rdvs.liste_rdv'))

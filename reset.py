from app import app
from models.db import db

# Script pour réinitialiser la base
with app.app_context():
    db.drop_all()    # Supprime toutes les tables existantes
    db.create_all()  # Recrée les tables selon les nouveaux modèles
    print("✔️ Base de données réinitialisée avec succès !")

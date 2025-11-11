from flask import Flask, render_template, request, redirect, url_for, flash
from config import Config
from models.db import db
from controllers.rdv_controller import rdv_bp
# Initialisation de l'application
app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'supersecretkey'  # Pour les messages flash
# Initialisation de la base de données
db.init_app(app)
# Enregistrer le blueprint des rendez-vous
app.register_blueprint(rdv_bp, url_prefix='/rdvs')
# Route pour la page d'accueil
@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crée les tables si elles n'existent pas
    app.run(debug=True, port=8000)


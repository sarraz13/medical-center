import os

class Config:
    SQLALCHEMY_DATABASE_URI = (
        "postgresql://postgres:szbn12345%3F@localhost:5432/medical_center"
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = "un_secret_key"



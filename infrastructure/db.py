from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def get_db():
    return db
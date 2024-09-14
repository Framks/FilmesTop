
class Config:
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@localhost:5432/films-top'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
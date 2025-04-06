from app import db

class Experiment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
    source = db.Column(db.String(128))
    publication = db.Column(db.String(128))
from app import db

class Link(db.Model):
    __tablename__ = 'links'

    pid = db.Column(db.Integer, primary_key=True)
    short = db.Column(db.String, nullable=False)
    long = db.Column(db.String, nullable=False)
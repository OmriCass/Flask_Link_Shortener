from app import db

class Link(db.Model):
    __tablename__ = 'links'

    pid = db.Column(db.Integer, primary_key=True)
    short = cd.Column(db.String, nullable=False)
    long = cd.Column(db.String, nullable=False)
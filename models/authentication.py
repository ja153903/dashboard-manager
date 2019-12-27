from extensions import db


class Authentication(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(100), primary_key=True)
    password = db.Column(db.String(28), nullable=False)

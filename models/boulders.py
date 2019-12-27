from extensions import db


class Boulders(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    grade = db.Column(db.String(3), nullable=False)
    attempts = db.Column(db.Integer, nullable=False)
    send = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("authentication.id"), nullable=False)

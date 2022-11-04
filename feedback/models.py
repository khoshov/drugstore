from extensions import db


class Feedback(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, nullable=False)
    text = db.Column(db.Text, nullable=False)


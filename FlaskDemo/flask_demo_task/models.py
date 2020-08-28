from flask_demo_task import db

class User(db.Model):
    email = db.Column(db.String(120), primary_key = True)
    name = db.Column(db.String(40), nullable=False)
    mobile_no = db.Column(db.String(20), nullable=False)
    company = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.mobile_no}', '{self.company}')"
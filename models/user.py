from models.shared_model import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)

    def __init__(self, latitude, longitude):
        self.latitude = latitude
        self.longitude = longitude

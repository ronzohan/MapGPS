import datetime
from sqlalchemy import TIMESTAMP
from shared_model import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    upload_time = db.Column(TIMESTAMP,default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    def __init__(self, latitude, longitude, upload_time=datetime.datetime.now()):
        self.latitude = latitude
        self.longitude = longitude
        self.upload_time = upload_time

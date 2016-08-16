from datetime import datetime
import bcrypt
from app import db

class Stop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    route = db.Column(db.String(80))
    tag = db.Column(db.String(80))
    direction = db.Column(db.String(80))
    title = db.Column(db.String(80))
    lat = db.Column(db.Float)
    lon = db.Column(db.Float)
    predictions = db.Column(db.PickleType)


    def __init__(self, route, tag, title, lat, lon):
        self.route = route
        self.tag = tag
        self.title = title
        self.lat = float(lat)
        self.lon = float(lon)
        self.direction = ''
        self.predictions = []

    def set_direction(self, direction):
        self.direction = direction 

    def update_predictions(self,predictions):
        self.predictions = predictions

    def __repr__(self):
        return '<Title %r>' % self.title
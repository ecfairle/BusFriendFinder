from datetime import datetime
import bcrypt

class Stop(object):


    def __init__(self, route, tag, title, lat, lon):
        self.route = route
        self.tag = tag
        self.title = title
        self.lat = float(lat)
        self.lon = float(lon)
        self.direction = None
        self.predictions = []

    def set_direction(self, direction):
        self.direction = direction 

    def update_predictions(self,predictions):
        self.predictions = predictions

    def __repr__(self):
        return '<Title %r>' % self.title
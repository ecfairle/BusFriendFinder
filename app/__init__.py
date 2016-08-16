import os
from flask import Flask
import numpy as np
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy(app)

from app.models import Stop

stop_list = np.array(Stop.query.all())
stop_locations = np.array([[stop.lat,stop.lon] for stop in stop_list])

from app import views
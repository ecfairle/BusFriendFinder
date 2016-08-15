import os
from flask import Flask
import numpy as np

app = Flask(__name__)
app.config.from_object('config')

from app import load_stops

stop_list = np.array(load_stops.collect_stops())

stop_locations = np.array([[stop.lat,stop.lon] for stop in stop_list])

from app import views
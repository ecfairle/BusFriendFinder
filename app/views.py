from flask import render_template, flash, redirect
from app import app
import nearby_predictions
import json
from flask import request

from sqlalchemy.ext.declarative import DeclarativeMeta
class AlchemyEncoder(json.JSONEncoder):
	def default(self, obj):
	    if isinstance(obj.__class__, DeclarativeMeta):
	        # an SQLAlchemy class
	        fields = {}
	        for field in [x for x in dir(obj) if not x.startswith('_') and x != 'metadata']:
	            data = obj.__getattribute__(field)
	            try:
	                json.dumps(data) # this will fail on non-encodable values, like other classes
	                fields[field] = data
	            except TypeError:
	                fields[field] = None
	        # a json-encodable dict
	        return fields

	    return json.JSONEncoder.default(self, obj)

@app.route('/')

@app.route('/index')
def index():
    location = [37.756722, -122.424454]
    stops = nearby_predictions.get_predictions(location)
    stops = [stop for stop in stops if stop.predictions]

    stops_json = [json.dumps(s,cls=AlchemyEncoder) for s in stops]

    return render_template('index.html', stops=stops[:10],stops_json=stops_json)
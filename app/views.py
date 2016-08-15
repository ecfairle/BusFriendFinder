from flask import render_template, flash, redirect
from app import app
import nearby_predictions
import json
from flask import request


@app.route('/')

@app.route('/index')
def index():
    location = [37.756722, -122.424454]
    stops = nearby_predictions.get_predictions(location)
    stops = [stop for stop in stops if stop.predictions]

    stops_json = [json.dumps(s,default=lambda o: o.__dict__) for s in stops]
    print(stops_json)
    return render_template('index.html', stops=stops[:10],stops_json=stops_json)



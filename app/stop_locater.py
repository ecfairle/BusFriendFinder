import numpy as np
from app import app
from app import stop_locations,stop_list


def closest_stops(location,n_stops):
	d = ((stop_locations-location)**2).sum(axis=1)
	ind = d.argsort()
	return top_unique_routes(ind,n_stops)

def top_unique_routes(ind,n_stops):
	discovered_stops = []
	for stop in stop_list[ind]:
		if not any(stop.route == s.route and stop.direction == s.direction for s in discovered_stops):
			discovered_stops.append(stop)
			if len(discovered_stops) == n_stops: return discovered_stops
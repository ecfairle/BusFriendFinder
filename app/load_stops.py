import sys
from .models import Stop
import xml_reader



def collect_stops():
	routes = get_routes()
	stops = []
	for route in routes:
		stops += get_stop_list(route)

	return stops


def get_stop_list(route):
	url = xml_reader.stop_list_url(route)
	stops_xml_dict = xml_reader.read_xml(url)

	raw_stop_list = stops_xml_dict['route']['stop']
	stop_list = [stop_to_obj(s,route) for s in raw_stop_list]

	directions = stops_xml_dict['route']['direction']
	set_directions(stop_list,directions)

	return stop_list


def set_directions(stop_list,directions):
	if isinstance(directions,dict):
		directions = [directions]

	for direction in directions:
		dir_title = direction['@title']
		stop_tags = [s['@tag'] for s in direction['stop']]
		for stop in stop_list:
			if stop.tag in stop_tags:
				stop.set_direction(dir_title)


def stop_to_obj(raw_stop, route):
	tag = raw_stop['@tag']
	title = raw_stop['@title']
	lat = raw_stop['@lat']
	lon = raw_stop['@lon']

	return Stop(route,tag,title,lat,lon)


def get_routes():
	url = xml_reader.routes_list_url()
	routes_xml_dict = xml_reader.read_xml(url)
	raw_routes_list = routes_xml_dict['route']
	routes_list = [r['@tag'].encode('ascii','ignore') for r in raw_routes_list]
	return routes_list

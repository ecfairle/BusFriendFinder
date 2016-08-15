import stop_locater
import xml_reader
from .models import Stop

def get_predictions(location,n_stops=20):
	stops = stop_locater.closest_stops(location,n_stops)
	url = xml_reader.multi_predictions_url(stops)
	pred_dict = xml_reader.read_xml(url)
	set_predictions(pred_dict, stops)

	return stops


def set_predictions(pred_dict, stops):
	route_groups = pred_dict['predictions']
	for route_group in route_groups:
		stop_tag = route_group['@stopTag']
		route_tag = route_group['@routeTag']
		try:
			direction = route_group['direction']['@title']
			times_list = get_times(route_group['direction'])
		except (KeyError, TypeError):
			continue
		stop = next((s for s in stops if s.tag == stop_tag and
			s.direction.find('Outbound') == direction.find('Outbound') and s.route == route_tag), None)
		if stop:
			print stop.tag
			stop.update_predictions(times_list)
		print times_list

	print '--------'



def get_times(route_group):
	times = []
	for prediction in route_group['prediction'][:2]:
		times.append(float(prediction['@minutes']))
	return times
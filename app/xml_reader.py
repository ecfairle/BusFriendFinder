import urllib2
import xmltodict

NEXTBUS_BASE_URI = 'http://webservices.nextbus.com/service/publicXMLFeed?'
AGENCY = 'sf-muni'


def read_xml(url):
	req = urllib2.Request(url, headers={'User-Agent' : 'Magic Browser'})
	con = urllib2.urlopen(req)

	data = con.read()
	con.close()
	dict = xmltodict.parse(data)['body']
	if 'Error' in dict:
		print('XML Retrieval Error')
		sys.exit()

	return dict


def stop_list_url(route):
	return '{}command=routeConfig&a={}&r={}&terse'.format(NEXTBUS_BASE_URI, AGENCY, route)

def routes_list_url():
	return '{}command=routeList&a={}'.format(NEXTBUS_BASE_URI, AGENCY)

def multi_predictions_url(stops):
	pred_template = '{}command=predictionsForMultiStops&a={}{}'
	stop_strs = ['&stops={}|{}'.format(stop.route,stop.tag) for stop in stops]
	return pred_template.format(NEXTBUS_BASE_URI,AGENCY,''.join(stop_strs))

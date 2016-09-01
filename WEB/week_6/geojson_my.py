import json
import urllib

serviceurl = "http://python-data.dr-chuck.net/geojson?"
while True:
	name = raw_input('Enter place name : ')
	if len(name) < 1: break

	url = serviceurl + urllib.urlencode(
	        {'sensor': 'false', 'address': name})

	print "Retrieving %s"%url
	connection = urllib.urlopen(url)
	raw_data = connection.read()
	print "Retrieved %d characters: "%len(raw_data)
	parsed_data = json.loads(raw_data)

	print "Place id", parsed_data["results"][0]["place_id"]
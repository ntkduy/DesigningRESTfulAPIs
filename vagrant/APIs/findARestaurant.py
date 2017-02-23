from geocode import getGeocodeLocation
import json
import httplib2

import sys
import codecs
sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

foursquare_client_id = "ZV1AQM0OCEU40QLOIT5AUQ0NGUGOUHWN3JXWGU2CVCQAFP14"
foursquare_client_secret = "DLJO4UP2NHIRNC4YNQRSNQZ0AZZBAFWGYY0AAYGX2553GERQ"


def findARestaurant(mealType,location):
	#1. Use getGeocodeLocation to get the latitude and longitude coordinates of the location string.
	latitude, longitude = getGeocodeLocation(location)
	#2.  Use foursquare API to find a nearby restaurant with the latitude, longitude, and mealType strings.
	#HINT: format for url will be something like https://api.foursquare.com/v2/venues/search?client_id=CLIENT_ID&client_secret=CLIENT_SECRET&v=20130815&ll=40.7,-74&query=sushi
	url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20170223&ll=%s,%s&query=%s' % (foursquare_client_id, foursquare_client_secret,latitude,longitude,mealType))
	
	h = httplib2.Http()
	result = json.loads(h.request(url,'GET')[1])
	if result['response']['venues']:
		#3. Grab the first restaurant
		restaurant 		= result['response']['venues'][0]
		venues_id 		= restaurant['id']
		venues_name 	= restaurant['name']
		venues_address 	= restaurant['location']['formattedAddress']
		address = ""
		for i in venues_address:
			address += i + " "
		venues_address 	= address
		#7. Return a dictionary containing the restaurant name, address
		restaurantInfo = {'name':venues_name, 'address':venues_address}
		print "Restaurant Name: %s" 	% restaurantInfo['name']
		print "Restaurant Address: %s" 	% restaurantInfo['address']
		return restaurantInfo
	else:
		print "No Restaurants Found for %s" % location
		return "No Restaurants Found"
		
	#4. Get a  300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
	#5. Grab the first image
	#6. If no image is available, insert default a image url
if __name__ == '__main__':
	findARestaurant("Pizza", "Tokyo, Japan")



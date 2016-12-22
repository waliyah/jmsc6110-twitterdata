#import JSON
try:
 	import json
except ImportError:
 	import simplejson as json

#import twitter libs
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

import config
import csv
import os.path
import sys
import codecs


# Get the Twitter data for each user in the list
def get_twitter_data():
	oauth= OAuth(config.ACCESS_TOKEN, config.ACCESS_SECRET, config.CONSUMER_KEY, config.CONSUMER_SECRET)

	#start twitter stream
	twitter = Twitter(auth=oauth)

	lists= 'jmsc6110-16-17'
	owner= 'waliyah_s'

	# get members
	result = twitter.lists.members(slug=lists,owner_screen_name=owner,count=200)

	user_data = []
	for theuser in result['users']:
		#print theuser['name']+' '+theuser['screen_name']+' '+str(theuser['id'])
		user = twitter.users.show(user_id=theuser['id'])
		#print user['name']+','+user['screen_name']+','+user['description']+str(user['followers_count'])+','+str(user['friends_count'])+','+str(user['favourites_count'])

		#print json.dumps(user)
		user_data.append(user)

	return user_data


def csv_write(data_python):
	csv_out = open('students_activity.csv', mode='w') #opens csv file
	writer = csv.writer(csv_out) #create the csv writer object

	fields = ['name', 'screen_name', 'description', 'followers_count', 'friends_count', 'retweet_count', 'favourites_count'] #field names
	writer.writerow(fields) #writes field

	for line in data_python:
	    #writes a row and gets the fields from the json object
	    #screen_name and followers/friends are found on the second level hence two get methods
	    writer.writerow([line.get('name').encode('unicode_escape'),
	                     line.get('screen_name').encode('unicode_escape'),
	                     line.get('description').encode('unicode_escape'), #unicode escape to fix emoji issue
	                     line.get('followers_count'),
	                     line.get('friends_count'),
	                     line.get('retweet_count'),
	                     line.get('favorite_count')])

	csv_out.close()


#-----------------------------------------------------------------------------------



	
if( not os.path.isfile('raw_user_data.json') ): 
	data_json = get_twitter_data()
	# print data_json
	# sys.exit()

	# with open('raw_user_data.json', 'w') as outfile:
 #    	json.dump(data_json, outfile, indent=4, sort_keys=True, separators=(',', ':'), ensure_ascii=False)\

	with codecs.open('raw_user_data.json', 'w', 'utf8') as f:
		f.write(json.dumps(data_json, sort_keys = True, ensure_ascii=False))
	f.close()
else:
	data_json = open('raw_user_data.json', mode='r').read() #reads in the JSON file into Python as a string
	data_python = json.loads(data_json) #turns the string into a json Python object
	csv_write(data_python)


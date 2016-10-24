 #import JSON
try:
 	import json
except ImportError:
 	import simplejson as json

#import twitter libs
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

import config


oauth= OAuth(config.ACCESS_TOKEN, config.ACCESS_SECRET, config.CONSUMER_KEY, config.CONSUMER_SECRET)

#start twitter stream
twitter = Twitter(auth=oauth)

lists= 'jmsc6110-16-17'
owner= 'waliyah_s'
#take sample
result = twitter.lists.members(slug=lists,owner_screen_name=owner)

#print tweets
#tweet_count = 100
#for tweet in iterator:
#	tweet_count -= 1
print json.dumps(result)

#	if tweet_count <=0:
#		break


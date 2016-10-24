 #import JSON
try:
 	import json
except ImportError:
 	import simplejson as json

#import twitter libs
from twitter import Twitter, OAuth, TwitterHTTPError, TwitterStream

ACCESS_TOKEN = '45837594-GceTeVW27iGhKeHOjv5lykJgHBHMeE7ijSrESFZ3T'
ACCESS_SECRET = 'yYx6HrAauAiCzXxajSojRYmo1BHNTcUlP6UFI0D5uB8zN'
CONSUMER_SECRET = 'IVBmTDlat4AahGX2uUV2gs9paugD4lGYDC7V9dqRc2oXQPBukY'
CONSUMER_KEY = 'iEsQzjEd7SpKDZzR59NjbrVGq'

oauth= OAuth(ACCESS_TOKEN,ACCESS_SECRET, CONSUMER_KEY, CONSUMER_SECRET)

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


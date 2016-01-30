from twitter import *

import requests
import urllib2

config = {}
execfile("config.py", config)

twitter = Twitter(
		        auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))


query = twitter.followers.ids()

search_for = 'healthcare'

List_ofIds = query[u'ids']

statuses = {}

trackID = []

for i in List_ofIds:

#-----------------------------------------------------------------------
# query the user timeline.
# twitter API docs:
# https://dev.twitter.com/rest/reference/get/statuses/user_timeline
#-----------------------------------------------------------------------
	results = twitter.statuses.user_timeline(user_id = i)

	for status in results:
		if search_for in status["text"]:
			trackID.append(i)


#-----------------------------------------------------------------------
# loop through each status item, and print its content.
#-----------------------------------------------------------------------
# for status in statuses.keys():
# 	print "(%s) %s" % (status["created_at"], status["text"].encode("ascii", "ignore"))

print trackID

twitter.direct_messages.new(
user_id= trackID[0],
text="I think yer swell!")
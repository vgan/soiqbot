from __future__ import print_function
import tweepy
from stackauth import StackAuth
from stackexchange import Site, StackOverflow, Sort, DESC
from soiq_keys import *
import logging

auth = tweepy.OAuthHandler(twitter_consumer_key, twitter_consumer_secret)
auth.set_access_token(twitter_token_key, twitter_token_secret)
api = tweepy.API(auth)
so = Site(StackOverflow)
logger = logging.getLogger()
logger.setLevel(logging.INFO)

def handler(event, context):
	question = so.questions(sort=Sort.Activity, order=DESC)[0]
        title= question.title
        url = question.url
	tweetbody = "nope"
	tags = ""
	for tag in question.tags:
        if tag eq "raku":
            tag = (tags + "#rakulang ")
        else:
		    tags = (tags + "#" + tag + " ")

		longbody = title + "\n" + url  + "\n" + tags
		longbodynourl = title  + "\n" + tags
	shortbody = title[:119] + "\n" + url
	if len(longbodynourl) >= 119:
       		tweetbody = shortbody
	else:
		tweetbody = longbody
	if tweetbody != 'nope':
		try:
        		status = api.update_status(status=tweetbody)
        	except:
        		print(' tweet failed')
	else:
		print( " tweetbody = nope. not tweeting")

	logger.info('got event{}'.format(event))
	logger.error('something went wrong')

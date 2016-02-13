#!/usr/bin/env python
import tweepy
from random import randint
import os
import urllib2
from slackbot_keys import *
from time import sleep

auth = tweepy.OAuthHandler(TWITTER_API_KEY,TWITTER_API_SECRET)
auth.set_access_token(TWITTER_TOKEN,TWITTER_TOKEN_SECRET)
api = tweepy.API(auth)

slackteam = 'sonicforum' 
slackchannel = 'bot-garden'
owner = 'vgan'
slug = 'vgan-bots'
basedir = '/home/vgan/slackbot/'
sinceidfile = basedir + 'sinceid.txt'
pacing = 3 # Posts to slack  every 3 seconds during loop
howmany = 20 # how many tweets to pull

slackboturl = 'https://' + slackteam + '.slack.com/services/hooks/slackbot?token=' + SLACK_TOKEN + '&channel=%23' + slackchannel

sinceID = open(sinceidfile, 'r')
since_id = sinceID.readline()
sinceID.close()

tweets = api.list_timeline(owner, slug, since_id=since_id,per_page=howmany,page='1')
total = len(tweets)
if total > 0:
	for tweet in tweets:
		user = str(tweet.user.screen_name)
		tweetid = str(tweet.id_str)
		tweeturl = 'https://twitter.com/' + user + "/status/" + tweetid
		print tweeturl
		request = urllib2.Request(slackboturl, tweeturl)
		response = urllib2.urlopen(request)
		sleep(pacing)
	mostrecentid = tweets[0].id_str
	sinceID = open(sinceidfile,"w+")
	sinceID.write(mostrecentid)
	sinceID.close()


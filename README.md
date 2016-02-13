# twitter-list-timeline-slackbot
Python script to pull tweets from a twitter list timeline and post them to a slack channel.

Requirements:
Tweepy and a Slackbot Key.

Note:
The script uses a file called sinceid.txt to store the id of the most recent tweet to use as a starting point on the next run.
You will need to manually select a tweet id from your list timeline to choose a starting point for the first run.

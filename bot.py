from secret import ACCESS_SECRET, ACCESS_TOKEN, CONSUMER_KEY, CONSUMER_SECRET
import tweepy as ty
import random
import csv
import os, sys
import time
import requests
import json

#start time from OS
starttime=time.time()

#Authorizes the code
auth = ty.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = ty.API(auth)

#Set Users , default value of tweet id's
screen_name = [["<enter user>",'1'] , ["<enter user>",'2']]

#Create User output CSV files
i = 0 
while i < len(screen_name):
	f = open('%s_Tweets.csv' % screen_name[i][0], 'wb')
	writer = csv.writer(f)
	writer.writerow(["Tweet", "Created_at" , "Tweet ID"])
	i += 1
	
def getUsersTweet(api):
	global message
	i = 0 
	while i < len(screen_name):
		old_id = screen_name[i][1]										# Loop through users, terminal and into uniq csv
		user = screen_name[i][0]
		r = api.user_timeline(user , count = 1 ,tweet_mode='extended')  # count sets the no of tweets to rx
		User_Tweets = r[0]
		User_Tweet = User_Tweets.full_text.encode("utf-8")
		screen_name[i][1] =  "[" + str(User_Tweets.id) + "]"
		message = ("Username: " + str(user) + "\nTweet: " + str(User_Tweet))
		if screen_name[i][1] == old_id:									# Loop through tweet id untill user sends new tweet
			print "No new Tweets, sleep +4 min"							# if id's are same pass
			pass
		else:															# new id means new tweet, post tweet
			print message
			#Output tweets to CSV file 
			f = open('%s_Tweets.csv' % user, 'a+')
			writer = csv.writer(f)
			writer.writerow([User_Tweet, User_Tweets.created_at , screen_name[i][1] ])
		i += 1

while True: 
	#Main Driver Script
	if __name__ == "__main__":
		getUsersTweet(api)
		time.sleep(240.0 - ((time.time() - starttime) % 240cal.0))				# Sets the time for the script to sleep , change both numbers , 5 = 5secs

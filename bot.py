from secret import ACCESS_SECRET, ACCESS_TOKEN, CONSUMER_KEY, CONSUMER_SECRET
import tweepy as ty
import random
import csv
import os, sys
import time

#start time from OS
starttime=time.time()

User_Tweet_id = 0
User_Tweet = ''
Notify = False

#Authorizes the code
auth = ty.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = ty.API(auth)

#Set Users
screen_name = ['<enter screen name>' , '<enter screen name>']

#Create User output CSV files
for user in screen_name:
	f = open('%s_Tweets.csv' % user, 'wb')
	writer = csv.writer(f)
	writer.writerow(["Tweet", "Created_at" , "Tweet ID"])

def getUsersTweet(api):
	global message
	global User_Tweet_id
	global User_Tweet
	for user in screen_name:  							
		r = api.user_timeline(user , count = 1)  		# count sets the no of tweets to rx
		i = 0
		while i < len(r):
			User_Tweets = r[i]
			User_Tweet = User_Tweets.text.encode("utf-8")
			User_Tweet_id =  "[" + str(User_Tweets.id) + "]"
			message = ("Username: " + str(user) + "\nTweet: " + str(User_Tweet))
			if Notify == True:
				print "printing"
				#Output tweets to CSV file 
				f = open('%s_Tweets.csv' % user, 'a+')
				writer = csv.writer(f)
				writer.writerow([User_Tweet, User_Tweets.created_at , User_Tweet_id ])
			i += 1

while True: 
	#Main Driver Script
	if __name__ == "__main__":
		old_id = User_Tweet_id
		getUsersTweet(api)
		time.sleep(6.0 - ((time.time() - starttime) % 6.0))	# Sets the time for the script to sleep , change both numbers , 5 = 5secs
		if User_Tweet_id == old_id:				# Loop through tweet id untill user sends new tweet
			print "No new Tweets +6 sec"			# if id's are same pass
			Notify = False
			pass
		else:							# new id means new tweet, post tweet
			print message
			Notify = True

			
			


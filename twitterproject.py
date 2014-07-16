#!/usr/bin/python3.4
from twitter import *
def main():
	OAUTH_TOKEN = '589023564-8FRScgrrSv3eTdvxpBNEIekF1Y4yMGnqfB9NeRCN'
	OAUTH_SECRET = 'XVlZJYQVYtRwfljdkqn4riNpeH9jb4BBSFXa6E4kPHK8O'
	CONSUMER_KEY = 'xWsph8bnDb7qNXPoKjnB0TwWz'
	CONSUMER_SECRET = '40b7HIuYiyfcZ1CdXM4g6oVNbzbCmjigSlEHZSq0shFfROW9P1'
	file_object = open('tweets.txt','w')
	t = Twitter(
            auth=OAuth(OAUTH_TOKEN, OAUTH_SECRET,
                       CONSUMER_KEY, CONSUMER_SECRET)
           )
	i = 1
	while(i < 11):
		t.statuses.update(
    		status= "This is the status number "+str(i))
		i = i + 1
	#file_object.write(str(t.statuses.home_timeline()))
main()
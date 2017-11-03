#!/usr/bin/env python
from twython import Twython
from bs4 import BeautifulSoup
import urllib2, random, sys, re

def sendTweet(tweetStr):
	apiKey = 'your_key_here'
	apiSecret = 'your_key_here'
	accessToken = 'your_key_here'
	accessTokenSecret = 'your_key_here'

	api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret)
	
	api.update_status(status=tweetStr)
	print("Tweeted: " + tweetStr)

def getQuote():
	url = "http://www.imdb.com/title/tt0374900/quotes"
	page =  urllib2.urlopen(url)
	soup = BeautifulSoup(page)


	quotes = [quote.split(":") for quote in re.findall('class="character"[^"]+</p>',str(soup))]
	quote_info = random.choice(quotes)
	quote = quote_info[1].split("<")[0].strip()
	character = quote_info[0].split(">")[1].replace("</span", "")
	
	return "\"" + quote + "\" - " + character

def saveTweet(tweetStr):
	file = open("bot_tweets.txt", "a")
	file.write(tweetStr + "\n")
	file.close()

def checkTweets(tweetStr, file_name):
	file = open(file_name, "r")
	file_contents = file.readlines()
	file.close()
	
	tweeted = False

	if tweetStr in file_contents:
		tweeted = True
	return tweeted

#main
tweet = getQuote()
saveTweet(tweet)
tweeted = checkTweets(tweet, "bot_tweets.txt")

while tweeted:
	tweet = getQuote()
	tweeted = checkTweets(tweet, "bot_tweets.txt")
sendTweet(tweet)		


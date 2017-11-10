#!/usr/bin/env python
from twython import Twython
from bs4 import BeautifulSoup
import urllib2, random, sys, re
from keys import *

def sendTweet(tweetStr):
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


#main
tweet = getQuote()
sendTweet(tweet)		


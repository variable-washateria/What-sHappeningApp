from urllib import request
import requests
from bs4 import BeautifulSoup
import lxml
import re
import urllib.request 



def numaddition(bandname):
	a = bandname + "bandname you chose:"  
	return a

def task2check(argument):
	b = argument + "task2works"
	return b


def querysearch(searchitem):
	print(searchitem + "   blahblahblah")
	search = searchitem

	
	url = "https://www.youtube.com/results?search_query=" + search 
	req = requests.get(url)
	soup = BeautifulSoup(req.text, 'html.parser')

	walloftext = soup.find(text=re.compile("videoId"))
	pattern = re.compile(r'(videoIds":..)(\w+)')
		#(/w)')


	lnks = []
	matches = pattern.finditer(walloftext)
	for match in matches:
		link = match.group(2)
		lnks.append(link)
			

	lnks = list(set(lnks))
	lnks = lnks[0:4]
	print(lnks)

	link = str(lnks[0]) 

	return lnks








		

from urllib import request
import requests
from bs4 import BeautifulSoup
import lxml
import re


##The question is how can I do specific query from form without circular imports? This current strategy is overkill.


# Mohawk 
def mohawkdictionary(date):
	print(date)
	url = "http://www.mohawkaustin.com/events/"
	req = requests.get(url)
	soup = BeautifulSoup(req.content, 'html.parser')

	# I. Dates

	# dates with days
	lstofdates = []
	alldates = soup.find_all('span','dates')
	for date in alldates:
		lstofdates.append(date.string)

	# eliminating the day
	lstofdates2 = []
	for el in lstofdates:
		lstofdates2.append(el[-6:])

	# elongating month name to standardize
	lstofdates3 = []
	for el in lstofdates2:
		if "Jan" in el:
			newel = el.replace("Jan","January")
		elif "Feb" in el:
			newel = el.replace("Feb","February") 
		elif "Mar" in el: 
			newel = el.replace("Mar","March")
		elif "Apr" in el: 
			newel = el.replace("Apr","April")
		if "May" in el: 
			newel = el.replace("May","May")
		elif "Jun"  in el: 
			newel = el.replace("Jun","June")
		elif "Jul" in el: 
			newel = el.replace("Jul","July")
		elif "Aug" in el: 
			newel = el.replace("Aug","August")
		elif "Sep" in el: 
			newel = el.replace("Sep","September")
		elif "Oct" in el: 
			newel = el.replace("Oct","October")
		elif "Nov" in el: 
			newel = el.replace("Nov","November")
		elif "Dec" in el: 
			newel = el.replace("Dec","December")
		elif " Jan" in el:
			newel = el.replace(" Jan","January")
		elif "Feb" in el:
			newel = el.replace(" Feb","February") 
		elif " Mar" in el: 
			newel = el.replace(" Mar","March")
		elif " Apr" in el: 
			newel = el.replace(" Apr","April")
		if " May" in el: 
			newel = el.replace(" May","May")
		elif " Jun"  in el: 
			newel = el.replace(" Jun","June")
		elif " Jul" in el: 
			newel = el.replace(" Jul","July")
		elif " Aug" in el: 
			newel = el.replace(" Aug","August")
		elif " Sep" in el: 
			newel = el.replace(" Sep","September")
		elif " Oct" in el: 
			newel = el.replace(" Oct","October")
		elif " Nov" in el: 
			newel = el.replace(" Nov","November")
		elif " Dec" in el: 
			newel = el.replace(" Dec","December")
		lstofdates3.append(newel)

	# II. Artists
	
	allshows = soup.find_all('h1', "event-name headliners")

	lstofshows = []
	for show in allshows:
		lstofshows.append(show.string)


	# III. Dictionary

	mohawkdict = dict(zip(lstofdates3, lstofshows)) 

	# IV. Arist on Date if Artist on Date

	if date in lstofdates3:
		mohawkband = mohawkdict[date] 
		return mohawkband
	else:
		mohawkband = "No bands playing at Mohawk that night."
		return mohawkband

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~") 

# Parish 

def parishdictionary(date):

	url = "https://www.theparishaustin.com/"
	req = requests.get(url)
	soup = BeautifulSoup(req.content, 'html.parser')

	# I. Dates

	# dates with year
	lstofdates = []
	c= soup.find_all('span', 'tw-event-date')
	for el in c:
		lstofdates.append(el.string)

	# eliminating the year
	lstofdates2 = []
	for el in lstofdates:
		lstofdates2.append(el[:-6])

	# II. Artists
	lstofartists = []
	a = soup.find_all('div', 'tw-name')
	for el in a:
		lstofartists.append(el.a.string)

	# III. Dictionry 

	parishdict = dict(zip(lstofdates2, lstofartists))
	print(parishdict)
	# return parishdict

	# IV. Arist on Date if Artist on Date

	if date in lstofdates2:
		parishband = parishdict[date] 
		return parishband
	else:
		parishband = "No bands playing at Parish that night."
		return parishband 





print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~" *10)




instance = parishdictionary("dummy data")

#curious why not work 
#ind = -1
#for el in instance:
#	ind +=1
#	if "May" in el:
#		instance.pop(ind)
#		ind -= 1
#print(instance)




#curiosity for what does "descndants" mean
#print(zoom1)
#print("~~~~~~~~~~~~~~~")
#zoom2 = zoom1.descendants
#lst =[]
#for el in zoom2:#
#	lst.append(el.string)    
#print(lst)
#date = lst[3]
#print(date)














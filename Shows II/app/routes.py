from app import app
from app.tasks import mohawkdictionary, parishdictionary
from app.tasks2 import numaddition, querysearch, task2check

from flask import render_template, request, url_for
from flask_wtf import FlaskForm
from wtforms import widgets, SelectMultipleField

placer2 = "Friends"


@app.route("/")
def home():
	return render_template("home.html")


@app.route("/tasks")
def test():
	return mohawkshow

@app.route("/yourresults", methods=['GET', 'POST'])
def yourresults():
	if request.method == 'POST':
		# from home html form 
		checked_venues = request.form.getlist("venue")
		date = request.form.get("date")

		if "Mohawk" in checked_venues:
			# tasks.py
			mohawkband = mohawkdictionary(date)
			# tasks2.py
			Mlstoflinks = querysearch(mohawkband)

		if "Parish" in checked_venues:
			# tasks.py
			parishband = parishdictionary(date)
			# tasks2.py
			Plstoflinks = querysearch(parishband)

		return render_template("yourresults.html", checked_venues = checked_venues, mohawkband= mohawkband, 
			parishband = parishband, theywantasee3 = placer2, date = date, Mlstoflinks = Mlstoflinks, Plstoflinks = Plstoflinks)
	else:
		return "hi"	


#May be obsolete soon: 
@app.route("/listen1/<searchitem>")
def listen1(searchitem):
	#bandname = request.args.get("bandname")
	bandname = "This is " 
	task2a = numaddition(bandname)

	searchitem = searchitem
	task2b = querysearch(searchitem)

	return render_template('listen1.html', searchitem = searchitem, somelamenum = task2a, thirdprint = task2b)



@app.route("/shows")
def shows():
	return render_template("shows.html")


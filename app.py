from chalice import Chalice
import requests
import re

app = Chalice(app_name='analyzer')
rating = 0

@app.route('/')
def index():
	return "index"

#@app.route('/get_rating')
#def get_rating():
#	global rating
#	return rating

@app.route('/get_userstories')
def get_userstories():
	url = "https://api.trello.com/1/lists/5a9cfda59445da34626f6f98/cards?fields=name"
	querystring = {"key":"dbbba347ce643d02d2ec025f566b80ad","token":"ef7788180b4052c7cdcfdae3276435f93b9cb554d04b75da5d37b327a339d04d"}
	response = requests.request("GET", url, params=querystring)
	data = response.json()
	return data

@app.route('/set_rating')
def set_rating():
	#rating = get_rating()
	global rating
	userstories = get_userstories()
	data = []
	for v in userstories:
		rating += 5
		data.append({'Userstory': v['name'], 'Rating': rating})
	return data

@app.route('/check_role')
def check_role():
	global rating
	userstories = get_userstories()
	data = []
	for v in userstories:
		#print v['name']
		rating = 0
		searchrole = re.search(r'As a', v['name'])
		if searchrole:
			#print 'Role was found.'
			rating += 5
			#break
		else:
			return 'Role was not found.'
		data.append({'Userstory': v['name'], 'Rating': rating})
	return data

@app.route('/check_feature')
def check_feature():
	global rating
	userstories = get_userstories()
	check_role()
	data = []
	for v in userstories:
		#print v['name']
		rating = 0
		searchfeature = re.search(r'I want to', v['name'])
		if searchfeature:
			#print 'Feature was found.'
			rating += 5
			#break
		else:
			print 'Feature was not found.'
		data.append({'Userstory': v['name'], 'Rating': rating})
	return data

@app.route('/check_length')
def check_length():
	userstories = get_userstories()
	data = []
	for v in userstories:
		length_userstory = len(v['name'])
		if length_userstory > 20:
			data.append({'Userstory': v['name'], 'Rating': 'Good Userstory'})
		else:
			return 'Bad Userstory'
	return data

@app.route('/test')
def test():
	test = "asdasd"
	return test
	
@app.route('/test2')
def test2():
	get_test = test()
	return get_test


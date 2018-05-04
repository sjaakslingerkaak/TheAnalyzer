from chalice import Chalice
import requests

app = Chalice(app_name='analyzer')

@app.route('/')
def index():
	return "index"

@app.route('/get_userstories')
def get_userstories():
	url = "https://api.trello.com/1/lists/5a9cfda59445da34626f6f98/cards?fields=name"
	querystring = {"key":"dbbba347ce643d02d2ec025f566b80ad","token":"ef7788180b4052c7cdcfdae3276435f93b9cb554d04b75da5d37b327a339d04d"}
	response = requests.request("GET", url, params=querystring)
	data = response.json()
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


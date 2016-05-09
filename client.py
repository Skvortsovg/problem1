import requests


link = 'http://127.0.0.1:4000'
while True:
	sleepTime = input('sleep time = ')
	priority = input('priority = ')
	data = (('sleepTime', sleepTime), ('priority', priority))
	r = requests.get(link, data)

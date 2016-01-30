#! /usr/bin/env python
import requests
import json

query = raw_input('Please enter a query:')

query = query.replace(" ", "+")

r = requests.get('https://hackathon.fiscalnote.com/bills?q='+ query +'&apikey=ZYPENE28RUZFRHIWFHVYI6CZL6MLAUGM')

#print r.text
jsonlist = json.loads(r.text)

for item in jsonlist:
	print 'Title: ', item['title']
	print 'State: ', item['state']
	print 'Description: ', item['description']
	print 'Current Status: ', item['current_status']
	print 
	print

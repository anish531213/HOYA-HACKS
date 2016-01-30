import requests
import urllib2
import json

header = {'Content-Type': 'json'}




data = {'q': 'heathcare', 
		 'legislature': 'US',
		 }

r = requests.get('https://hackathon.fiscalnote.com/bills?q=rights&apikey=ZYPENE28RUZFRHIWFHVYI6CZL6MLAUGM')

text = json.loads(r)

print text
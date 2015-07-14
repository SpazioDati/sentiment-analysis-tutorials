# coding: utf-8
import logging
from bs4 import BeautifulSoup
import requests

logging.captureWarnings(True)

APP_ID='INSERT_YOUR_APP_ID'
APP_KEY='INSERT_YOUR_APP_KEY'
SERVICE='sent'

APPSTORECC='it'
APPSTOREID='507269919'

r = requests.get('https://itunes.apple.com/{}/rss/customerreviews/id={}/xml'.format(APPSTORECC,APPSTOREID))
soup = BeautifulSoup(r.text)

for entry in soup.select('entry')[:10]:
	for content in entry.select('content[type="text"]'):
		r = requests.get('https://api.dandelion.eu/datatxt/sent/v1', { '$app_id':APP_ID, '$app_key':APP_KEY, 'text':content.string, 'lang':'it' }, verify=False)
		sent=r.json()
		print "[{}]".format(sent['sentiment']['score']), content.string


import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from apiclient.discovery import build
googlesearch = build("customsearch", "v1",
               developerKey="AIzaSyAwS_D5vFkfqzz-6LcfUtcxEOTd-mFp5qs")

def doImageSearch(searchString):
	results = googlesearch.cse().list(
		q=searchString,
		cx='011321095650785962352:3h3forz45xu',
		searchType='image',
		num=1,
		safe= 'off'
	).execute()
	
	if not 'items' in results:
		return ''
	else:
		#for item in results['items']:
		item = results['items'][0]
		return item['link'].encode('utf-8')
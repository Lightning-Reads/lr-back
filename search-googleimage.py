from apiclient.discovery import build
googlesearch = build("customsearch", "v1",
               developerKey="AIzaSyAwS_D5vFkfqzz-6LcfUtcxEOTd-mFp5qs")

def doImageSearch(searchString):
	results = googlesearch.cse().list(
		q=searchString,
		cx='011321095650785962352:3h3forz45xu',
		searchType='image',
		num=3,
		safe= 'off'
	).execute()
	
	if not 'items' in res:
		print 'No result !!\nres is: {}'.format(res)
	else:
		#for item in res['items']:
		item = res['items'][0]
		return item['link'].encode('utf-8')
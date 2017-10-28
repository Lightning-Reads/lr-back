from wikiapi import WikiApi
wiki = WikiApi({ 'locale' : 'en'}) # to specify your locale, 'en' is default

def doSearch(searchString):
    results = wiki.find(searchString)
    article = wiki.get_article(results[0])
    response = {}
    response['key'] = searchString
    response['url'] = article.url
    response['image'] = article.image
    # print response
    return response

# bo = doSearch('Barack Obama')
# ny = doSearch('New York')

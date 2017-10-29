from wikiapi import WikiApi

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

wiki = WikiApi({ 'locale' : 'en'}) # to specify your locale, 'en' is default

def getWikipediaLink(searchString):
    try:
        results = wiki.find(searchString)
        if not results:
            print 'No result !!\nresults is: {}'.format(results)
            return {}
        else:
            article = wiki.get_article(results[0])
            if not article.url:
                print 'No result !!\narticle is: {}'.format(article)
                return {}
            else:
                return  article.url
    except:
        print "Something went wrong"
        return {}

# bo = doSearch('Barack Obama')
# print bo
# bo2 = doSearch('afdopsakfdskfasdf adfadfsadf')
# print bo2
# ny = doSearch('New York')
# print ny

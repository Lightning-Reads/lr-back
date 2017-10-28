import pickle
from eventregistry import *
from pprint import pprint
import time
from datetime import date
from datetime import timedelta




def doArticleSearch(searchString):
    try:
        enddate = date.today()
        startdate = enddate - timedelta(days=7)  # decrease day by one

        er = EventRegistry(apiKey = "66fe2cd6-4a41-40f7-b62a-35e1d2bfed6e")

        q = QueryArticles(
           conceptUri = er.getConceptUri(searchString),
           dateStart = startdate,
           dateEnd = enddate,
           lang = "eng")
            
        q.setRequestedResult(RequestArticlesInfo(page = 1, count = 10,sortBy="rel", returnInfo = ReturnInfo(articleInfo = ArticleInfoFlags(
            bodyLen = 1500,
            basicInfo = True,
            title = True,
            body = True,
            eventUri = True,
            concepts = False,
            storyUri = True,
            duplicateList = False,
            originalArticle = False,
            categories = True,
            location = False,
            image = False,
            extractedDates = False,
            socialScore = True,
            details = False))))            

        res = er.execQuery(q)

        article = res['articles']['results'][0]
        title = article['title']
        body  = article['body']
        datetime = article['dateTime']
        sharesFB = 0
        if "facebook" in article['shares']:
            sharesFB=article['shares']['facebook']
        sharesLI = 0
        if "linkedIn" in article['shares']:
            sharesLI=article['shares']['linkedIn']
        sharesGO = 0
        if "googlePlus" in article['shares']:
            sharesGO=article['shares']['googlePlus']
        url = article['url']
        wgt=article['wgt']
        source_id = 0
        if "id" in article['source']:
            source_id=article['source']['id']
        source_name = 0
        if "title" in article['source']:
            source_name=article['source']['title']
        categories = ""
        categories_id = ""

        return article
        
    except ValueError, e:
        return ''

#test        
news = doArticleSearch("Germany")

print news['title']


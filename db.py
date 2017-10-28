import pickle
from eventregistry import *
import mysql.connector
from mysql.connector import errorcode
from pprint import pprint
import time
from datetime import date
from datetime import timedelta

#from pprint_data import data


try:
    cnx = mysql.connector.connect(user='textanalysis', password='textanalysissis',
                              host='2fast2furiouz.no-ip.info',
                              database='textanalysis')                    
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exists")

    else:
        print(err)
else:

    startdate = datetime.date.today()

    er = EventRegistry(apiKey = "66fe2cd6-4a41-40f7-b62a-35e1d2bfed6e")
    cursor = cnx.cursor()
    q = QueryArticles(
       conceptUri = er.getConceptUri("Bitcoin"),
       dateStart = startdate,
       dateEnd = startdate,
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

    add_article = ("INSERT INTO datatable "
                    "(title, body, datetime, sharesFB, sharesLI, sharesGO, isDuplicate, url, id_EventReg, wgt, source_id, source_name, categories, categories_id) "
                    "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)")                       
    for article in res['articles']['results']:    
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
        isDuplicate = 1 if article['isDuplicate'] else 0
        url = article['url']
        id_EventReg=article['id']
        wgt=article['wgt']
        source_id = 0
        if "id" in article['source']:
            source_id=article['source']['id']
        source_name = 0
        if "title" in article['source']:
            source_name=article['source']['title']
        categories = ""
        categories_id = ""
        for category in article['categories']:
            categories = categories + category['uri'] + ", "
            categories_id = categories_id + str(category['id']) + ", "
            
        data_article = (title, body, datetime, sharesFB, sharesLI, sharesGO, 
                        isDuplicate, url, id_EventReg, wgt, source_id, source_name, categories, categories_id)
        cursor.execute(add_article, data_article)
        emp_no = cursor.lastrowid
        cnx.commit()


            
    #    delstatmt = "DELETE a FROM `datatable` as a, `datatable` as b" + \
    #               " WHERE (a.`title`   = b.`title` OR a.`title` IS NULL AND b.`title` IS NULL)" + \
    #               " AND (a.`body` = b.`body` OR a.`body` IS NULL AND b.`body` IS NULL)" + \
    #                " AND a.ID > b.ID;"
    #    cursor.execute(delstatmt)
    #    cnx.commit()
            
            
        
    cursor.close()
    cnx.close()    

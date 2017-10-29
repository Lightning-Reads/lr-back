# -*- coding: utf-8 -*-

from searchWikipedia import getWikipediaLink
from searchGoogleimage import doImageSearch
from importantWords import getWordCloud
from operator import itemgetter

from searchGoogletext import getTextTopic, doSentimentAnalysis, getMostRelevantEvent, getMostRelevantEntity, getMostRelevantLocation

upperBound = 1


def generateContent(originalContent):

    count = 0
    # mockData = {'Hackathon': 0.03434,
    #             'SAP': 0.111,
    #             'Jan Böhmermann': 0.001}

    originalContent.decode("utf-8")

    wordlist = getWordCloud(originalContent)
    # wordlist = mockData

    wordlist = sorted(wordlist.iteritems(), key=itemgetter(1), reverse=True)

    result = {}
    result['baseText'] = originalContent
    result['importantWords'] = []
    result['helpfulLinks'] = []
    result['imageLinks'] = []
    result['meta'] = {}

    result['meta']['sentiment'] = doSentimentAnalysis(originalContent)
    result['meta']['person'] = getMostRelevantEntity(originalContent)
    result['meta']['location'] = getMostRelevantLocation(originalContent)
    result['meta']['event'] = getMostRelevantEvent(originalContent)
    result['meta']['topic'] = getTextTopic(originalContent)


    for key, value in wordlist:
        result['importantWords'].append({
            'word': key,
            'importance':  value})
        if count < upperBound:
            result['helpfulLinks'].append({
                'word': key,
                'url': getWikipediaLink(key)})
            result['imageLinks'].append({
                'word': key,
                'url': doImageSearch(key)})
            count = count + 1

    return result


#data = generateContent("afja fsfjasfd ü adsfadsf")


# Nachricht umwandeln (unicode -> Ausgabe-Encoding) und
# mit print an die Standardausgabe übergeben.
# print data

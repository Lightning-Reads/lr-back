# -*- coding: utf-8 -*-

from searchWikipedia import getWikipediaLink
from searchGoogleimage import doImageSearch


def generateContent(originContent):

    mockData = {'Hackathon': 0.03434,
                'SAP': 0.111,
                'Jan Böhmermann': 0.001}

    originContent.decode("utf-8")

    # wordlist = getWordlist(originContent)
    wordlist = mockData

    result = {}
    result['baseText'] = originContent
    result['importantWords'] = []
    result['helpfulLinks'] = []
    result['imageLinks'] = []

    for key, value in wordlist.iteritems():
        result['helpfulLinks'].append({
            'word': key,
            'url': getWikipediaLink(key)})
        result['importantWords'].append({
            'word': key,
            'importance':  value})
        result['imageLinks'].append({
            'word': key,
            'url': getWikipediaLink(key)})

    return result


#data = generateContent("afja fsfjasfd ü adsfadsf")


# Nachricht umwandeln (unicode -> Ausgabe-Encoding) und
# mit print an die Standardausgabe übergeben.
# print data

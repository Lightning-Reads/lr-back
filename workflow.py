# -*- coding: utf-8 -*-
from multiprocessing import Pool, TimeoutError, Process, freeze_support
from searchWikipedia import getWikipediaLink
from searchGoogleimage import doImageSearch
from importantWords import getWordCloud
from textSummarize import summarize
from searchNews import doArticleSearch
from operator import itemgetter
from db import db_getAllCounter

import time
import os

from searchGoogletext import getTextTopic, doSentimentAnalysis, getMostRelevantEvent, getMostRelevantEntity, getMostRelevantLocation

upperBound = 5


def getBounds(category):
    result = db_getAllCounter(category)
    print result


def generateContent(originalContent):

    pool = Pool(processes=16)              # start 16 worker processes

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
    result['summary'] = summarize(originalContent)
    result['meta'] = {}

    mostImportantWord = wordlist[0][0]
    print mostImportantWord

    # # runs in *only* one process
    # ressentiment = pool.apply_async(doSentimentAnalysis, (originalContent,))
    # resMostRelevantEntity = pool.apply_async(
    #     getMostRelevantEntity, (originalContent,))      # runs in *only* one process
    # # runs in *only* one process
    # res3 = pool.apply_async(getMostRelevantLocation, (originalContent,))
    # # runs in *only* one process
    # res4 = pool.apply_async(getMostRelevantEvent, (originalContent,))
    # # runs in *only* one process
    # res5 = pool.apply_async(getTextTopic, (originalContent,))

    res6 = pool.apply_async(doArticleSearch, (mostImportantWord,))

    # try:
    #     result['meta']['sentiment'] = ressentiment.get(timeout=30)
    # except TimeoutError:
    #     print "We lacked patience and got a multiprocessing.TimeoutError"
    #     result['meta']['sentiment'] = []

    # try:
    #     result['meta']['person'] = resMostRelevantEntity.get(timeout=0)
    # except TimeoutError:
    #     print "We lacked patience and got a multiprocessing.TimeoutError"
    #     result['meta']['person'] = []

    # try:
    #     result['meta']['location'] = res3.get(timeout=0)
    # except TimeoutError:
    #     print "We lacked patience and got a multiprocessing.TimeoutError"
    #     result['meta']['location'] = []

    # try:
    #     result['meta']['event'] = res4.get(timeout=0)
    # except TimeoutError:
    #     print "We lacked patience and got a multiprocessing.TimeoutError"
    #     result['meta']['event'] = []

    # try:
    #     result['meta']['topic'] = res5.get(timeout=0)
    # except TimeoutError:
    #     print "We lacked patience and got a multiprocessing.TimeoutError"
    #     result['meta']['topic'] = []

    # try:
    #     result['meta']['news'] = res6.get(timeout=0)
    # except TimeoutError:
    #     print "We lacked patience and got a multiprocessing.TimeoutError"
    #     result['meta']['news'] = []

    result['meta']['sentiment'] = doSentimentAnalysis (originalContent)
    result['meta']['person'] = getMostRelevantEntity (originalContent)
    result['meta']['location'] = getMostRelevantLocation (originalContent)
    result['meta']['event'] = getMostRelevantEvent (originalContent)
    result['meta']['topic'] = getTextTopic (originalContent)
    result['meta']['news'] = doArticleSearch (mostImportantWord)

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

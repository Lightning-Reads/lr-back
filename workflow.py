# -*- coding: utf-8 -*-
from multiprocessing import Pool, TimeoutError, Process, freeze_support
from searchWikipedia import getWikipediaLink
from searchGoogleimage import doImageSearch
from importantWords import getWordCloud
from textSummarize import summarize
from operator import itemgetter
import time
import os

from searchGoogletext import getTextTopic, doSentimentAnalysis, getMostRelevantEvent, getMostRelevantEntity, getMostRelevantLocation

upperBound = 5

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
    result['summary']  = summarize(originalContent)
    result['meta'] = {}

    ressentiment = pool.apply_async(doSentimentAnalysis, (originalContent,))      # runs in *only* one process
    resMostRelevantEntity = pool.apply_async(getMostRelevantEntity, (originalContent,))      # runs in *only* one process
    res3 = pool.apply_async(getMostRelevantLocation, (originalContent,))      # runs in *only* one process
    res4 = pool.apply_async(getMostRelevantEvent, (originalContent,))      # runs in *only* one process
    res5 = pool.apply_async(getTextTopic, (originalContent,))      # runs in *only* one process
    
    try:
        result['meta']['sentiment'] = ressentiment.get(timeout=20)
    except TimeoutError:
        print "We lacked patience and got a multiprocessing.TimeoutError"
        
    try:
        result['meta']['person'] = resMostRelevantEntity.get(timeout=0)
    except TimeoutError:
        print "We lacked patience and got a multiprocessing.TimeoutError"
        
    try:
        result['meta']['location'] = res3.get(timeout=0)
    except TimeoutError:
        print "We lacked patience and got a multiprocessing.TimeoutError"
        
    try:
        result['meta']['event'] = res4.get(timeout=0)
    except TimeoutError:
        print "We lacked patience and got a multiprocessing.TimeoutError"
        
    try:
        result['meta']['topic'] = res5.get(timeout=0)
    except TimeoutError:
        print "We lacked patience and got a multiprocessing.TimeoutError"
    

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

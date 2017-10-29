#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Imports the Google Cloud client library

import six

from google.cloud import language_v1beta2
from google.cloud.language_v1beta2 import enums
from google.cloud.language_v1beta2 import types

import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "TextAnalyzer-b3c6791872a9.json"
# entity types from enums.Entity.Type
entity_type = ('UNKNOWN', 'PERSON', 'LOCATION', 'ORGANIZATION',
               'EVENT', 'WORK_OF_ART', 'CONSUMER_GOOD', 'OTHER')


def doSentimentAnalysis(searchString):
    try:
        askstr = searchString.encode('utf-8')
        print askstr

        document = types.Document(
            content=askstr,
            type=enums.Document.Type.PLAIN_TEXT)

        # Instantiates a client
        client = language_v1beta2.LanguageServiceClient()

        sentiment = client.analyze_sentiment(
            document=document).document_sentiment

        #print('Text: {}'.format(text))
        #print('Sentiment: {}, {}'.format(sentiment.score, sentiment.magnitude))
        print str(sentiment.score)
        return ((str(sentiment.score), str(sentiment.magnitude)))
    except ValueError, e:
        return ''


def doEntitiyAnalysis(searchString):
    try:
        """Detects entities in the text."""
        client = language_v1beta2.LanguageServiceClient()

        if isinstance(searchString, six.binary_type):
            text = searchString.decode('utf-8')

        # Instantiates a plain text document.
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT)

        # Detects entities in the document. You can also analyze HTML with:
        #   document.type == enums.Document.Type.HTML
        entities = client.analyze_entities(document).entities

        for entity in entities:
            print('=' * 20)
            print(u'{:<16}: {}'.format('name', entity.name))
            print(u'{:<16}: {}'.format('type', entity_type[entity.type]))
            print(u'{:<16}: {}'.format('metadata', entity.metadata))
            print(u'{:<16}: {}'.format('salience', entity.salience))
            print(u'{:<16}: {}'.format('wikipedia_url',
                                       entity.metadata.get('wikipedia_url', '-')))

    except ValueError, e:
        return ''


def getMostRelevantEntity(searchString):
    try:
        """Detects entities in the text."""
        client = language_v1beta2.LanguageServiceClient()

        # if isinstance(searchString, six.binary_type):
        text = searchString.decode('utf-8')

        # Instantiates a plain text document.
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT)

        # Detects entities in the document. You can also analyze HTML with:
        #   document.type == enums.Document.Type.HTML
        entities = client.analyze_entities(document).entities

        for entity in entities:
            if entity_type[entity.type] == 'PERSON':
                return_entity = entity
                break

        result = {
            'name': entity.name,
            'salience': entity.salience,
            'wikipedia_url': entity.metadata.get('wikipedia_url', '-')
        }
        return result

    except ValueError, e:
        return ''


def getMostRelevantLocation(searchString):
    try:
        """Detects entities in the text."""
        client = language_v1beta2.LanguageServiceClient()

        # if isinstance(searchString, six.binary_type):
        text = searchString.decode('utf-8')

        # Instantiates a plain text document.
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT)

        # Detects entities in the document. You can also analyze HTML with:
        #   document.type == enums.Document.Type.HTML
        entities = client.analyze_entities(document).entities

        for entity in entities:
            if entity_type[entity.type] == 'LOCATION':
                return_entity = entity
                break

        result = {
            'name': entity.name,
            'salience': entity.salience,
            'wikipedia_url': entity.metadata.get('wikipedia_url', '-')
        }
        return result

    except ValueError, e:
        return ''


def getMostRelevantEvent(searchString):
    try:
        """Detects entities in the text."""
        client = language_v1beta2.LanguageServiceClient()

        #if isinstance(searchString, six.binary_type):
        text = searchString.decode('utf-8')

        # Instantiates a plain text document.
        document = types.Document(
            content=text,
            type=enums.Document.Type.PLAIN_TEXT)

        # Detects entities in the document. You can also analyze HTML with:
        #   document.type == enums.Document.Type.HTML
        entities = client.analyze_entities(document).entities

        for entity in entities:
            if entity_type[entity.type] == 'EVENT':
                return_entity = entity
                break
            
        result = {
            'name': entity.name,
            'salience': entity.salience,
            'wikipedia_url': entity.metadata.get('wikipedia_url', '-')
        }
        return result

    except ValueError, e:
        return ''


def getTextTopic(searchString):
    try:
        """Classifies content categories of the provided text."""
        client = language_v1beta2.LanguageServiceClient()

        document = types.Document(
            content=searchString,
            type=enums.Document.Type.PLAIN_TEXT)

        categories = client.classify_text(document).categories

        print categories

        # for category in categories:
        if not categories:
            return []
        else :
            category = {
                'name': categories[0].name,
                'confidence' : categories[0].confidence
            }
            return category

        # return category
        #print(u'=' * 20)
        #print(u'{:<16}: {}'.format('name', category.name))
        #print(u'{:<16}: {}'.format('confidence', category.confidence))

    except ValueError, e:
        return ''



# tests
#getTextTopic("Mariano Rajoy, Spain's prime minister, announced the immediate dismissal of the Catalan government and parliament, and called a fresh regional election for December 21st.")

# return_entity = getMostRelevantLocation(
#     "Mariano Rajoy, Spain's prime minister, announced the immediate dismissal of the Catalan government and parliament, and called a fresh regional election for December 21st.")
# print(u'{:<16}: {}'.format('name', return_entity.name))

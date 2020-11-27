import nltk
from nltk.stem.lancaster import LancasterStemmer
stemmer = LancasterStemmer()

import numpy
import tflearn
import tensorflow
import random
import json


words = []
tags = []
docs = []

with open('intents.json') as file:
    data = json.load(file)
    intents = data['intents']

for intent in intents:
    for pattern in intent['patterns']:
        wordList = nltk.word_tokenize(pattern)
        words.extend(wordList);
        docs.append(pattern)

        if intent['tag'] not in tags:
            tags.append(intent['tag'])

print(docs)
print()
print(intents)
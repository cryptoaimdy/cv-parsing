# -*- coding: utf-8 -*-
"""
Created on Mon Sep 16 21:41:18 2019

@author: Ali
"""

import re
import nltk
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('averaged_perceptron_tagger')
from nltk.corpus import stopwords
stop = stopwords.words('english')
from nltk.corpus import wordnet


file = open('003.txt', encoding="utf8")
my_corpus = file.read()

new_corpus = my_corpus.lower()
#rmoving special chars
result = re.sub('[^A-Za-z0-9]+',' ', new_corpus)
#removing nmbrs
result = re.sub(r'[0-9]+', '', result)
                             
Sentences = nltk.sent_tokenize(result)
Tokens = []
for Sent in Sentences:
    Tokens.append(nltk.word_tokenize(Sent)) 
Words_List = [nltk.pos_tag(Token) for Token in Tokens]

Nouns_List = []

for List in Words_List:
    for Word in List:
        if re.match('[NN.*]', Word[1]):
             Nouns_List.append(Word[0])

Names = []
for Nouns in Nouns_List:
    if not wordnet.synsets(Nouns):
        Names.append(Nouns)

print (Names)
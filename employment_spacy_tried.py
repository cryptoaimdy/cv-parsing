# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 13:12:30 2019

@author: Ali
"""
import re
import spacy
nlp = spacy.load('en_core_web_sm')
from collections import Counter

file = open('resume.txt', encoding="utf8")
my_corpus = file.read()

corpus_text = nlp(my_corpus)
sentences = list(corpus_text.sents)


for sentence in sentences:
     print (sentence)
     
      
for token in corpus_text:
     print (token, token.idx)
     

words = [token.text for token in corpus_text
          if not token.is_stop and not token.is_punct]
word_freq = Counter(words)
# 100 commonly occurring words with their frequencies
common_words = word_freq.most_common(100)
print (common_words)

unique_words = [word for (word, freq) in word_freq.items() if freq == 2]
print (unique_words)
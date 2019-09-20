# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 17:10:14 2019

@author: Ali
"""
import re
import string
import spacy
from spacy.matcher import Matcher
file = open('018.txt', encoding="utf8")
my_corpus = file.read()

new_corpus = my_corpus.lower()
#rmoving special chars
result = re.sub('[^A-Za-z0-9]+',' ', new_corpus)


#removing nmbrs
#result = re.sub(r'[0-9]+', '', result)
                             

pattern = "professional experience ([\s\S]*?) professional training |\
employment history ([\s\S]*?) skills and interests|\
professional experience ([\s\S]*?) education |\
employment ([\s\S]*?) personal information |\
work experience ([\s\S]*?) education |\
previous employment ([\s\S]*?) reference |\
employment to date ([\s\S]*?) further skills |\
experience ([\s\S]*?) reference |\
experience ([\s\S]*?) references |\
employment ([\s\S]*?) activities |\
employment history ([\s\S]*?) reference |\
employment history ([\s\S]*?) referees |\
career history ([\s\S]*?) referees"
match = re.findall(pattern, result)

final =  match
print(final)

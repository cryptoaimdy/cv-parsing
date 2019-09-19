# -*- coding: utf-8 -*-
"""
Created on Thu Sep 19 17:10:14 2019

@author: Ali
"""
import re
file = open('resume.txt', encoding="utf8")
my_corpus = file.read()

pattern = "\.?(?P<sentence>.*?PROFESSIONAL TRAINING*?)\."
match = re.search(pattern, my_corpus)
if match != None:
    sentence = match.group("sentence")
    
print(sentence)
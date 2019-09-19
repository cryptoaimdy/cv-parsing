# -*- coding: utf-8 -*-
"""
Created on Tue Sep 17 17:11:01 2019

@author: Ali
"""
import re



file = open('resume.txt', encoding="utf8")
my_corpus = file.read()


email_pattern = re.compile(r'[a-zA-Z0-9_\.]+@[a-zA-Z-\.]*\.(com|edu|net|us|org|eu|co.in|in)')
phone_pattern = re.compile(r'[(][\d]{3}[)][]\- []?[\d]{3}-[\d]{4}')
email_matches = email_pattern.finditer(my_corpus)
number_matches = phone_pattern.finditer(my_corpus)

for emails in email_matches:
    print(emails)
    
for number in number_matches:
    print(number.group(0))
    
    

print(emails.)
    
    



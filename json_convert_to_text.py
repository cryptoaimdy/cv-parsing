# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:23:06 2019

@author: Ali
"""







import json, codecs

data = []
with open('resume.json', encoding = 'utf-8') as f:
    for line in f:
        data.append(json.loads(line))

for content in data['content']:
    print('content')
with open('data.txt', 'wb') as f:
    json.dump(data[content], codecs.getwriter('utf-8')(f), ensure_ascii=False, indent=4)
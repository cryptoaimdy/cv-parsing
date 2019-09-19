# -*- coding: utf-8 -*-
"""
Created on Wed Sep 18 22:23:06 2019

@author: Ali
"""

import json
with open('Entity.json') as f:
    data = json.load(f)
# Output: {'name': 'Bob', 'languages': ['English', 'Fench']}
print(data)
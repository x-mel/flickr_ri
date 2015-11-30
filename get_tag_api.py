# -*- coding: utf-8 -*-
"""
Created on Sun Nov  8 10:03:50 2015

@author: mel
"""

import pickle
from numpy import *
import flickrapi
import json

# key 1
api_key = u'5683bi###a7c225e0ff3ae47a726ea375'
api_secret = u'bcee7###c1697a43'

flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')

# load the list of ids dumped previously into a file
with open('list_id', 'rb') as f:
    lid = pickle.load(f)

for i in arange(0, 800000, 10000):
    ltag=[]
    for pid in lid[i:i+10000]:
        ltag.append(flickr.photos.getInfo(photo_id=pid))
    # list of ids dumped into a file
    with open('list_tags_'+str(i+1), 'wb') as f:
        pickle.dump(ltag, f)


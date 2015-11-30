# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import pickle
#from sys import getsizeof
from numpy import arange
import flickrapi
#import json

api_key = u'4296c###3da6302e2f98dea40a375892c1'
api_secret = u'3066###bb41bce26'

flickr = flickrapi.FlickrAPI(api_key, api_secret, format='parsed-json')

# number of pages that have our results
npages = flickr.photos.search(tags='barcelona', per_page=500, sort='relevance').get('photos').get('pages')

# Total number of photos with tag Barcelona
totalp = flickr.photos.search(tags='barcelona', page=0, per_page=500, sort='relevance').get('photos').get('total')

print(npages)
print(totalp)

# list of pages number to iterate on
lpages=arange(1, npages+1)
lid=[]

# getting the info and saving the phptp id and username in lid
for i in lpages:
    info = flickr.photos.search(tags='barcelona', page=i, per_page=500, sort='relevance').get('photos').get('photo')
    lid+=[[item['owner'],item['id']] for item in info]
# list of ids dumped into a file
with open('list_id', 'wb') as f:
    pickle.dump(lid, f)


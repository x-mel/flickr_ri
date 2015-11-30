# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 21:44:08 2015

@author: mel
"""
import pickle
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import json
#import time

with open('list_id', 'rb') as f:
        lid = pickle.load(f)

driver = webdriver.PhantomJS()
wait = WebDriverWait(driver, 10)

date_xpath= "/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div[2]/div/span"
tag_xpath= "/html/body/div[1]/div/div[3]/div/div[2]/div[4]/div[1]/ul/li/a[2]"

data=[]

for i in lid:    
    driver.get('https://www.flickr.com/photos/'+i[0]+'/'+i[1])
    element = wait.until(EC.presence_of_element_located((By.XPATH, tag_xpath)))
    # Note that we used find_elements_by_xpath with an S, because there are different tags
    # This returns a list of tags. 
    tag = driver.find_elements_by_xpath(tag_xpath)
    # We extract the text part of the tags and save it in a list
    # We get the date uploaded
    date= driver.find_element_by_xpath(date_xpath)
    # Instead of getting the text (which is the date taken) we get the date uploaded which is
    # included in the title attribute    
    data+= [{'id': i[1], 'user' : i[0], 'posted' : date.get_attribute("title"), 'tags' : [tag_text.text for tag_text in tag]}]

driver.quit()

with open('flickr_data_pickle', 'wb') as fudge:
    pickle.dump(data, fudge)

with open('flickr_data.json', 'a+') as fap:
    json.dump(data, fap)

"""
start = time.time()

t=[['129582710@N06', '22734724280'], ['49912151@N08', '22503441277'], ['7617410@N02', '22911234641'], ['43742357@N03', '22461866828'], ['128356571@N08', '22456705187'], ['48377137@N05', '22880615101'], ['43742357@N03', '22436775668'], ['42343095@N08', '22228650093'], ['49912151@N08', '22848321625'], ['129582710@N06', '22823108605']]

# We start the web driver
driver = webdriver.PhantomJS()
# Setting up a condition for the webrowser to wait
wait = WebDriverWait(driver, 10)

date_xpath= "/html/body/div[1]/div/div[3]/div/div[2]/div[1]/div[2]/div/span"
tag_xpath= "/html/body/div[1]/div/div[3]/div/div[2]/div[4]/div[1]/ul/li/a[2]"

list_tags =[]
list_date=[]

for i in t:
    u= i[0]
    p= i[1]
    
    driver.get('https://www.flickr.com/photos/'+u+'/'+p)
    element = wait.until(EC.presence_of_element_located((By.XPATH, tag_xpath)))
    
    # Note that we used find_elements_by_xpath with an S, because there are different tags
    # This returns a list of tags. 
    tag = driver.find_elements_by_xpath(tag_xpath)
    # We extract the text part of the tags and save it in a list
    tags = [tag_text.text for tag_text in tag]
    list_tags.append(tags)
    
    # We get the date uploaded
    date= driver.find_element_by_xpath(date_xpath)
    # Instead of getting the text (which is the date taken) we get the date uploaded which is
    # included in the title attribute
    list_date.append(date.get_attribute("title"))

driver.quit()
print(time.time()-start)
"""
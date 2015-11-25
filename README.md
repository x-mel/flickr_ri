#Contributors
```
Ahmad Mel 	
Carlos Soler
Pau Hernández
Reza Attar
Shahin Ashkiani
```
#Overview
 
##Abstract: Is Barcelona more Spanish, Catalan or International city?
Our project explore the rise of nationalism and the idea of independence of Catalunya, in Barcelona, over
the past few month. Our approach starts by getting a list of all the photos with the tag Barcelona from 
flickr, then get a list of the other tags for each of those photos, analyse the tags and perform different
inference on the data, and visualize the results in a classy way. 8D


##Goal
The goal of the project is to explore the political activism on one of the rising social media
platform Flickr, probing the evolution  of the Independencia movement in Catalunya over the past few months.
	

##Methodology

Getting the data: Flickr API or Web Crawling?
Flickr offers a large numbers of api for developers to explore. It's a great way of getting the data
without the need to build a crawler. Great right? But there is a catch. 
It has  a limited fetching speed. 
Basically flickr impose a limit on the numbers of requests per unit time, which is 3600 requests per hour. 
But this seems fast enough no?
Well flickr has around 4 millions photos with Barcelona. With a speed of 3600 requests/hr we will need
around 1000 hours of continuous running to get the information needed from each of those photos.
To solve this problem, we decided to build a crawler.
Our approach was, if we can get a list of all the photos' id with a Barcelona tag using an api, and then feed it to
the crawler, so it doesn't have to crawl all of flickr searching each photo for the Barcelona tag then
getting its data if it matches.



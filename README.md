#Contributors
Ahmad Mel  
Carlos Soler  
Pau Hernández  
Reza Attar  
Shahin Ashkiani

 
#Barcelona, in the flickr eye.
Exploring Barcelona from a flickr perspective, socially and politically.
Our approach starts by getting a list of all the photos with the tag Barcelona from 
flickr, then get a list of the other tags for each of those photos, analyse the tags and perform different
inference on the data, and visualize the results in a classy way. :D

#Methodology

##Getting the data: Flickr API or Web Crawling?
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
So a crawler was built. After many struggles. As flickr implements dynamical page generation. In short, if you
want to get certain information from a page (including tags), this information is generated once a request is sent.
This poses a problem as it's more complicated to overcome this limitation without sacrificing the time. We used
a crawler written in python, using selenium, an api for web automation, and phantomjs a headless webdriver.
The process of getting one photo tho, takes around 2 times more than flickr api.  
The advantage of this method is that it can be parallelized, running on multiple machines.  
The data was exported, in 2 format, serialized python dictionary, and json file in the following format.  
{     
    user_id : #####,  
    date posted : ######,  
    photo_id : ######,  
    tags : [ ###, ####, .. ]             
}  
The date posted is in unix timestamp, to facilitate the analysis.
The json file is then analysed using R. 


#Pre-processing and analyzing the data

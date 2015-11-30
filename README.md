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
So we built our crawler using scrapy. After many struggles, as flickr implements dynamical page generation. In short, if you
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
We will do the pre-processing using R.  

Since the files were saved in a JSON format, we looked for a way of reading it in R. We found a package called "RJSONIO", whit which we were able to read the JSON files.  

Once we had the data loaded into R, we wanted to see the evolution of the mean of tags per picture of each year. While doing so, we found out that our data was mainly concentrated in 2014 (with some data in 2013 and 2015). We deduced that this was due to ordering the pictures by relevance (since the most relevant ones may be from 2014).  
Since we already had the data downloaded, we decided to analyze the year 2014 by months, instead of the evolution during the years.  

Then, we tried to create something similar to a Python dictionary (that is, a structure that stores a name (the tags, in this case) and a counter associated to it, which in our case means the number of times that this tag appears in our data), but in R. When we tried to do that, we found the problem that the loop is too resource consuming. Therefore, there arrives a moment (relatively soon) where the loop does not run anymore, so we will work around that.  

Once this is done, our next goal will be some ANOVA and clustering.  

For performing the ANOVA we are going to consider the structure that we have described aboved (the one that is similar to python dictionary) and by using it, we can see the evolution of different tags during time and then the ANOVA test will be able to tell us if there exist some real relationship between those tags.  
With this same objective (proof relationship between tags) we want to achieve some cluster study related with this tags, in concrete we want to compare the output we get by perfoming clutering ourselfs with the clutering provided by flickr (https://www.flickr.com/photos/tags/barcelona/clusters/) which does not seem suficient to us. In order to do this clustering we did some research and we found an interesting article directly related with our objectives.   

( http://bit.ly/1Yy3JCe )

#Visualization
To date, we're still experimenting with the data. Although we'll be using different visualization for different goals. One of the suggested representation of the evolution of the tags by month is the following script.\\
http://romsson.github.io/dragit/example/nations.html
Although not implemented yet, it will be used in our final presentation along with other interesting conclusion. Stay tuned!

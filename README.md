# Expedia's Tweets - Quotes - User Interface
This is an User Interface for the Expedia's Twitter feed to get the latest 8 tweets through a script which can be run again to get the updated tweets behind the scenes once the application starts. My main objective while solving this exercise was to focus on the correct display of data rather than fancy way to show it.  

The script [forms.py](https://github.com/sushantgupta1206/GUPSUS03part1/blob/master/ExpediaTwitterScrapper/forms.py) is the main python script to be run from a command line and it will start a server on the local host where the user is expected to to view the 8 most recent tweets by the expedia group. The script when executed, parses the previously created twitter's html page from the spider scrawl as explained in exercise01 and then lists down all the tweets stored in the html file. It then retrieves and renders the [expedia-tweets-html page](https://github.com/sushantgupta1206/GUPSUS03part1/blob/master/ExpediaTwitterScrapper/templates/expedia_tweets.html) on the localhost which displays tweets on the UI.      
  
  
**Technology Stack used :**   
> Python 2.7     
> Flask for UI creation
> wtform in python for verification  

**The Output and inferences :**   
  
Please check the output files in the output folder [here]https://github.com/sushantgupta1206/GUPSUS03part1/tree/master/Outputs) and the json object which the code generated [here] (https://github.com/sushantgupta1206/GUPSUS03part1/blob/master/ExpediaTwitterScrapper/Top_8_Tweets.json) to verify the correctness.   
  
**Steps to Run the code:**   
> 1. clone the repository using `git clonehttps://github.com/sushantgupta1206/GUPSUS03part1.git` on the local machine
> 2. Navigate to the folder \GUPSUS03part1\ExpediaTwitterScrapper  

IFF to update the tweets - follow step 3 otherwise skip to 4th step as the repository already has the last run top 8 tweets file. 
> 3. Same as Exercise 1:  
    3.a. install dependencies using `pip install bs4` for beautiful soup; `pip install Scrapy` for installing Scrapy  
    3.b. navigate the the '\GUPSUS01\ExpediaTwitterScrapper' folder and then run the spider by using `scrapy crawl expedia_spider` where expedia_spider is the name of the spider I use to scrape the Twitter feed of Expedia.  
    3.c. Make sure the 'Top_8_tweets.json' file is generated  
> 4. Install dependencies using `pip install flask` for the flask setup/ configuration; and `pip install wtforms` for the form validation library.  
> 4. Run the script `forms.py` by using `python forms.py`.
> 5. On the chrome/ IE browser please go the local host and port which the console specifies where the server starts: in my case it is 'http://127.0.0.1:5000/'
> 6. Press the 'Get Tweets' button and you should see the output or else it will throw invalid server/ html error.  


**Note:**  
> As a future improvement the UI can be made more decorative but currently it satisfies the requirement of clear readibility.
> Also, an aditional feature where the button click runs the file to update the tweets and then displays latest tweets without the user manually running the update script can be added.






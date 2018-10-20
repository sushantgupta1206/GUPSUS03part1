import scrapy
from bs4 import BeautifulSoup
# author : Sushant Gupta
# python file to scrap twitter feed and generate json output into a new file 
class ExpediaTweetsSpider(scrapy.Spider):
    # spider name
    name = "expedia_spider"

    def start_requests(self):
        urls = [
            'https://twitter.com/Expedia',
        ]
        # generating and passing requests
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)
    
    # parser funtion to parse the html response
    def parse(self, response):       
        document= BeautifulSoup(response.body, "html.parser")
        tweets = []
        tweet = {}
        count = 8
        # reading all tags
        for tag in document.find('ol', attrs = { "class" : "stream-items js-navigable-stream" }).findAll('li', attrs = {"data-item-type" : "tweet"}):
            content = tag.find('div', attrs = {"class" : "js-tweet-text-container"}).text.strip()
            tweet['content'] = content.encode('ascii', 'ignore')
            reply = tag.find('button', attrs = {"data-modal" : "ProfileTweet-reply"}).find('span', attrs = {"class":"ProfileTweet-actionCountForPresentation"}).text.strip()
            time = tag.find('a', attrs = {"class" : "tweet-timestamp js-permalink js-nav js-tooltip"})
            tweet['created_at'] = time['title'].encode('ascii', 'ignore')
            tweet['replys'] = reply.encode('ascii', 'ignore')
            retweet = tag.find('button', attrs = {"data-modal" : "ProfileTweet-retweet"}).find('span', attrs = {"class":"ProfileTweet-actionCountForPresentation"}).text.strip()
            tweet['retweets'] = retweet.encode('ascii', 'ignore')
            favorites = tag.find('button', attrs = {"class" : "ProfileTweet-actionButton js-actionButton js-actionFavorite"}).find('span', attrs = {"class":"ProfileTweet-actionCountForPresentation"}).text.strip()
            tweet['favorites'] = favorites.encode('ascii', 'ignore')
            tweets.append(tweet)
            tweet = {}
            count-=1
            # assuring top 8 tweets only
            if count ==0:
                break
                
        # generating the output file
        filename = "Top_8_Tweets.json"
        with open(filename, 'wb') as f:
            f.writelines("%s\n" % tweet for tweet in tweets)
        print ("### Scrapped Successfully. Please open the ",filename," file to check the Top 8 tweets ###")
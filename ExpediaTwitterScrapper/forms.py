# author : Sushant Gupta
# python file to display the results from the twitter feed in the form of JSON objects 
from flask import Flask, render_template, flash, request
from wtforms import Form, TextField, TextAreaField, validators, StringField, SubmitField
import requests
import scrapy
import json

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'
# I could have set the secret key in an environment variable and ask the reviewer to create his/ her own, 
#but doesn't really affect on using this hence I am sending the key as a part of the code itself 

@app.route("/", methods=['GET', 'POST'])
def hello():
    if request.method == 'POST':
       
        # code to get top 8 posts
        flash("Top 8 posts are : ")
        filename = "Top_8_Tweets.json"
        tweetFile = open(filename)
        tweets = tweetFile.readlines()

        # print tweets
        for tweet in tweets:

            one_tweet =""
            # initial verification
            print tweet[:-1]
            t = eval(tweet[:-1])
            for key,val in t.iteritems():
                one_tweet += "%s: %s\n" % (key,val) 
            flash(one_tweet)
    return render_template('expedia_tweets.html')
 
if __name__ == "__main__":
    app.run()

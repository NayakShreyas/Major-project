from tkinter import *
import tkinter as tk
import csv
import tweepy


class twitter_search_Hashtag(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self.query = StringVar()
        self.label = Label(self, text="Search Twitters By the Query or Hashtag").pack()
        self.entry = Entry(self, textvariable=self.query).pack()

        def search_Hashtag():
            # Copying all the aceess code and secrets
            consumer_key = "km4nSAsQtGR4zpTQk9P424TWY"
            consumer_secret = "Xor6KLCzC4IrOFveNpVTx6yIVoW0v1cfN672xJ1PtOLDw4N1aF"
            access_token = "4638458112-R9uI1d5kv4mqiKTq6L21zGxqM76UA9XkSdnYHHJ"
            access_token_secret = "cOs5v6ui5E5v1oEXHBNqdPHgKyUCyXf2GxVT3hbqcMxQj"

            # Creating api object and authenticating
            # Creating the authentication object
            auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
            # Setting your access token and secret
            auth.set_access_token(access_token, access_token_secret)
            # Creating the API object while passing in auth information
            api = tweepy.API(auth)
            # The Twitter user who we want to get tweets from
            name = self.query.get()
            print(name)
            # Number of tweets to pull
            tweetCount = 20
            # Calling the user_timeline function with our parameters
            twitter_query = self.query.get()
            results = api.search(q=twitter_query, count=tweetCount)

            # Open/create a file to append data to
            filename = twitter_query + ".csv"
            csvFile = open(filename, 'a')

            # Use csv writer
            csvWriter = csv.writer(csvFile)

            # foreach through all tweets pulled
            for tweet in results:
                # printing the text stored inside the tweet object
                csvWriter.writerow(
                    [tweet.created_at, tweet.text.encode('utf-8'), tweet.retweet_count, tweet.favorite_count])
                print(tweet.text)

        self.button = Button(self, text="Search", command=search_Hashtag).pack()
        self.main_button = tk.Button(self, text="Go to the start page", command=lambda: controller.show_frame("main_page")).pack()
        return

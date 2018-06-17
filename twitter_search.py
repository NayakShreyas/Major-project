from tkinter import *
import tkinter as tk
import csv
import sys
import tweepy




'''def search_function():
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
    query = twitter_search.search_text.get()
    print(query)
    # Number of tweets to pull
    tweetCount = 200


    # Calling the user_timeline function with our parameters
    results = api.search(q=query, count=tweetCount)
    twitter_query = twitter_search.search_text.get()

    # Open/create a file to append data to
    filename = query + ".csv"
    csvFile = open(filename, 'a')

    # Use csv writer
    csvWriter = csv.writer(csvFile)

    # foreach through all tweets pulled
    for tweet in results:
        # printing the text stored inside the tweet object
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8'),tweet.retweet_count,tweet.favorite_count])
        print(tweet.text)
    return


def percentage(part,whole):
    return 100*float(part)/float(whole)'''

'''root=Tk()
search_text=StringVar()

root.geometry('450x450+500+300')
root.title("Twitter search")

mlabel=Label(root,text="Enter the query").pack()

search_entry=Entry(root,textvariable=search_text).pack()

mButton=Button(root,text="Search",command=search_function).pack()


root.mainloop()'''

class twitter_search(tk.Frame):

    def __init__(self,parent,controller):
        tk.Frame.__init__(self, parent)
        self.controller=controller
        search_text = StringVar()
        mlabel = Label(self, text="Select the Choice").pack()
        mButton = Button(self, text="Search by Person", command=lambda: controller.show_frame("twitter_search_Name")).pack()
        mButton = Button(self, text="Search by Hashtag/Query", command=lambda: controller.show_frame("twitter_search_Hashtag")).pack()


    def search_function():
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
        query = twitter_search.search_text.get()
        print(query)
        # Number of tweets to pull
        tweetCount = 200

        # Calling the user_timeline function with our parameters
        results = api.search(q=query, count=tweetCount)
        twitter_query = twitter_search.search_text.get()

        # Open/create a file to append data to
        filename = query + ".csv"
        csvFile = open(filename, 'a')

        # Use csv writer
        csvWriter = csv.writer(csvFile)

        # foreach through all tweets pulled
        for tweet in results:
            # printing the text stored inside the tweet object
            csvWriter.writerow(
                [tweet.created_at, tweet.text.encode('utf-8'), tweet.retweet_count, tweet.favorite_count])
            print(tweet.text)
        return

    def percentage(part, whole):
        return 100 * float(part) / float(whole)
#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt

passwd = input("Password: ")

reddit = praw.Reddit(client_id='fzr0BShtwiAr_w',
                     client_secret='7WR2TvbreQLYryJtTFSctL-heFU',
                     user_agent='Loota',
                     username='Loota-app',
                     password=passwd)

subNew = reddit.subreddit('Miniswap').new()

def scrape():
    postDict = {"title": [],
                "url": [],
                "created": [],
                "body": []}

    for submission in subNew:
        postDict["title"].append(submission.title)
        postDict["url"].append(submission.url)
        postDict["created"].append(submission.created)
        postDict["body"].append(submission.selftext)

    return postDict



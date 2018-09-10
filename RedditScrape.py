#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt

reddit = praw.Reddit(client_id='fzr0BShtwiAr_w',
                     client_secret='7WR2TvbreQLYryJtTFSctL-heFU',
                     user_agent='Loota',
                     username='Loota-app',
                     password='7227kfxx@')

subNew = reddit.subreddit('Miniswap').new()

def scrape():
    postDict = {}

    return postDict



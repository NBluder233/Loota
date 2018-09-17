#! usr/bin/env python3
import praw
import Alert
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

def parse(searchTerms):
    subDict = scrape()

    i = 0
    postList = []

    # Iterate through all scraped titles
    while i < len(subDict['title']):
        _titl = subDict['title'][i]
        have, want = "", ""

        # Search for faction
        # TODO: No hardcoded faction, switch between buying/selling
        if "ORK" in _titl.upper():
            if "[W]" in _titl.upper():
                have, want = _titl.upper().split("[W]")
            elif "(W)" in _titl.upper():
                have, want = _titl.upper().split("(W)")
            else:
                print(_titl)

            if "ORK" in have.upper():
                postList.append(i)
        i += 1

    for itm in postList:
        if searchTerms[0].upper() != "END":
            for term in searchTerms:
                if term.upper() in subDict['body'][itm]:
                    # Send on post info to alert function
                    Alert.TestAlert(subDict['title'][itm], subDict['url'][itm])
        else:
            Alert.TestAlert(subDict['title'][itm], subDict['url'][itm])

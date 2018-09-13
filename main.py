#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt
import RedditScrape as rdt
import Alert
import re


def _redParse(searchTerms):
    subDict = rdt.scrape()

    i = 0
    postList = []

    #Iterate through all scraped titles
    while i < len(subDict['title']):
        _titl = subDict['title'][i]

        #Search for faction
        #TODO: No hardcoded faction, switch between buying/selling
        if "CHAOS" in _titl.upper():
            postList.append(i)
        i += 1

    for itm in postList:
        if searchTerms[0].upper() != "END":
            for term in searchTerms:
                if term.upper() in subDict['body'][itm]:
                    #Send on post info to alert function
                    Alert.TestAlert(subDict['title'][itm], subDict['url'][itm])
        else:
            Alert.TestAlert(subDict['title'][itm], subDict['url'][itm])






def main():
    _redParse(["End"])


if __name__ == "__main__": main()

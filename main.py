#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt
import RedditScrape as rdt


def _redParse():
    subDict = rdt.scrape()

    i = 0
    while i < len(subDict['title']):
        _titl = subDict['title'][i]
        #print(_titl, "\n")
        if "ORKS" in _titl.upper():
            have, want = _titl.split("W")
            print("Have: ", have)
            print("Want: ", want)

        i += 1




def main():
    _redParse()


if __name__ == "__main__": main()
